-- 1️⃣ View: CustomerOrders
CREATE VIEW CustomerOrders AS
SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;


-- 2️⃣ Stored Procedure: AddNewOrder
DELIMITER //
CREATE PROCEDURE AddNewOrder(IN cust_id INT, IN prod_id INT, IN qty INT)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Customers WHERE customer_id = cust_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer does not exist!';
    ELSE
        INSERT INTO Orders (customer_id, product_id, quantity, order_date)
        VALUES (cust_id, prod_id, qty, NOW());
    END IF;
END;
//
DELIMITER ;


-- 3️⃣ Trigger: AfterOrderDelete
CREATE TABLE IF NOT EXISTS OrderLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    deleted_at DATETIME
);

DELIMITER //
CREATE TRIGGER AfterOrderDelete
AFTER DELETE ON Orders
FOR EACH ROW
BEGIN
    INSERT INTO OrderLogs(order_id, deleted_at)
    VALUES (OLD.order_id, NOW());
END;
//
DELIMITER ;


-- 4️⃣ Function: CalculateOrderTotal
DELIMITER //
CREATE FUNCTION CalculateOrderTotal(o_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(p.price * o.quantity)
    INTO total
    FROM Orders o
    JOIN Products p ON o.product_id = p.product_id
    WHERE o.order_id = o_id;
    RETURN IFNULL(total, 0);
END;
//
DELIMITER ;


-- 🔍 Testing
-- Add a new order
CALL AddNewOrder(1, 2, 5);

-- View customer orders
SELECT * FROM CustomerOrders;

-- Delete an order (logged automatically)
DELETE FROM Orders WHERE order_id = 3;

-- Calculate total for order
SELECT CalculateOrderTotal(1) AS TotalAmount;
