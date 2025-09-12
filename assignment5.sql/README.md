# Assignment 5: SQL Views, Stored Procedures, Triggers & Functions

## 📌 Description
This project demonstrates **advanced SQL programming techniques** by using:
- **Views** to simplify reporting queries
- **Stored Procedures** to automate operations
- **Triggers** to enforce business rules automatically
- **Functions** to create reusable calculations

---

## 🛠️ Features

### 1️⃣ View: `CustomerOrders`
Summarizes customers with the number of orders they made.

```sql
SELECT * FROM CustomerOrders;




2️⃣ Stored Procedure: AddNewOrder

Adds a new order only if the customer exists.

CALL AddNewOrder(1, 2, 5);

3️⃣ Trigger: AfterOrderDelete

Logs deleted orders into an audit table.

DELETE FROM Orders WHERE order_id = 3;
SELECT * FROM OrderLogs;

4️⃣ Function: CalculateOrderTotal

Computes the total amount of an order.

SELECT CalculateOrderTotal(1) AS TotalAmount;

📊 What I Learned

How to simplify queries with Views

How to automate processes with Stored Procedures

How to enforce rules with Triggers

How to reuse logic with Functions

This assignment demonstrates practical, real-world SQL development skills used in professional environments.


