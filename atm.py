class BankATM:
    def __init__(self, pin, balance=0):
        self._pin = str(pin)
        self._balance = balance

    def _authenticate(self):
        for _ in range(5):
            entered_pin = input("Enter PIN: ")
            if entered_pin == self._pin:
                return True
            print("Incorrect PIN")
        print("Account locked.")
        return False

    def _display_menu(self):
        return input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nChoose option: ")

    def _check_balance(self):
        print(f"Current Balance: ₹{self._balance:.2f}")

    def _deposit(self):
        amount = input("Enter amount to deposit: ")
        try:
            amount = float(amount)
            if amount > 0:
                self._balance += amount
                print("Deposited successfully.")
            else:
                print("Invalid amount. Must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def _withdraw(self):
        amount = input("Enter amount to withdraw: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Must be greater than zero.")
            elif amount > self._balance:
                print("Insufficient funds.")
            else:
                self._balance -= amount
                print("Withdrawal successful.")
        except ValueError:
            print("Please enter a number.")

    def run(self):
        if not self._authenticate():
            return
        while True:
            choice = self._display_menu()
            if choice == '1':
                self._check_balance()
            elif choice == '2':
                self._deposit()
            elif choice == '3':
                self._withdraw()
            elif choice == '4':
                print("Session ended.")
                break
            else:
                printt("Please select a valid option.")

atm = BankATM("9999", 6000)
atm.run()
