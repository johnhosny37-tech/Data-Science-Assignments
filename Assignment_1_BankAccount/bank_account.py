class BankAccount:
    def __init__(self, name, current_balance=0.0):
        self.name = name
        self.current_balance = current_balance

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.current_balance += amount
            print(f"✅ Deposit successful. New balance: {self.current_balance}")
        else:
            print("⚠️ Please enter a valid amount.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("⚠️ Please enter a valid amount.")
        elif self.current_balance >= amount:
            self.current_balance -= amount
            print(f"✅ Withdrawal successful. New balance: {self.current_balance}")
        else:
            print("❌ Insufficient funds.")

    def check_balance(self):
        """Display current balance"""
        print(f"💰 {self.name}, your current balance is: {self.current_balance}")


# ---------- Example Run ----------
if __name__ == "__main__":
    name = input("Hi, what is your name? ")
    try:
        balance = float(input("What is your current balance? "))
        account = BankAccount(name, balance)

        while True:
            action = input("\nDo you want to deposit, withdraw, check balance, or exit? ").lower()
            
            if action == "deposit":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif action == "withdraw":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif action == "check balance":
                account.check_balance()
            elif action == "exit":
                print("👋 Thank you for using our banking system.")
                break
            else:
                print("⚠️ Invalid action selected.")
    except ValueError:
        print("⚠️ Invalid balance entered.")
