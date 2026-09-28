class Customer:
    def __init__(self, name, phone, customer_id, salary):
        self.name = name
        self.phone = phone
        self.customer_id = customer_id
        self.salary = salary

    def display_customer(self):
        print("\n----- CUSTOMER DETAILS -----")
        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)
        print("Phone       :", self.phone)
        print("Salary      : ₹", self.salary)


class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def display_account(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer.name)
        print("Balance        : ₹", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("₹", amount, "deposited successfully.")
            print("New Balance : ₹", self.balance)
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")
            print("Remaining Balance : ₹", self.balance)

    def check_balance(self):
        print("Current Balance : ₹", self.balance)


class Card:
    def __init__(self, card_number, customer):
        self.card_number = card_number
        self.customer = customer

    def display_card(self):
        print("Card Number :", self.card_number)
        print("Customer    :", self.customer.name)


class DebitCard(Card):
    def display_card(self):
        print("\n----- DEBIT CARD -----")
        print("Card Number :", self.card_number)
        print("Customer    :", self.customer.name)


class CreditCard(Card):
    def __init__(self, card_number, customer, limit):
        super().__init__(card_number, customer)
        self.limit = limit

    def display_card(self):
        print("\n----- CREDIT CARD -----")
        print("Card Number :", self.card_number)
        print("Customer    :", self.customer.name)
        print("Credit Limit: ₹", self.limit)


class Loan:
    def __init__(
        self,
        customer,
        account,
        amount,
        interest_rate,
        minimum_salary,
        minimum_balance
    ):
        self.customer = customer
        self.account = account
        self.amount = amount
        self.interest_rate = interest_rate
        self.minimum_salary = minimum_salary
        self.minimum_balance = minimum_balance

    def verify_customer(self):
        print("\n----- LOAN VERIFICATION -----")
        print("Customer Salary :", self.customer.salary)
        print("Bank Balance    :", self.account.balance)
        print("Required Salary :", self.minimum_salary)
        print("Required Balance:", self.minimum_balance)

        if (
            self.customer.salary >= self.minimum_salary
            and self.account.balance >= self.minimum_balance
        ):
            print("\nSalary requirement satisfied.")
            print("Bank balance requirement satisfied.")
            print("LOAN APPROVED!")
            return True

        print("\nLoan verification failed.")

        if self.customer.salary < self.minimum_salary:
            print("Salary is below the required limit.")

        if self.account.balance < self.minimum_balance:
            print("Bank balance is below the required limit.")

        print("LOAN REJECTED!")
        return False

    def calculate_loan(self):
        if self.verify_customer():
            interest = self.amount * self.interest_rate / 100
            total = self.amount + interest

            print("\n----- LOAN DETAILS -----")
            print("Loan Amount   : ₹", self.amount)
            print("Interest Rate : ", self.interest_rate, "%")
            print("Interest      : ₹", interest)
            print("Total Amount  : ₹", total)


class GoldLoan(Loan):
    def __init__(self, customer, account, amount):
        super().__init__(
            customer,
            account,
            amount,
            8,
            20000,
            10000
        )


class CarLoan(Loan):
    def __init__(self, customer, account, amount):
        super().__init__(
            customer,
            account,
            amount,
            9,
            30000,
            25000
        )


class HomeLoan(Loan):
    def __init__(self, customer, account, amount):
        super().__init__(
            customer,
            account,
            amount,
            7,
            50000,
            50000
        )


print("================================")
print("       SIMPLE BANKING SYSTEM")
print("================================")

name = input("Enter customer name: ")
phone = input("Enter phone number: ")
customer_id = input("Enter customer ID: ")
salary = float(input("Enter monthly salary: ₹"))

customer = Customer(
    name,
    phone,
    customer_id,
    salary
)

account_number = input("Enter account number: ")
initial_balance = float(input("Enter current bank balance: ₹"))

account = Account(
    account_number,
    customer,
    initial_balance
)

debit_card = DebitCard(
    "XXXX-1111",
    customer
)

credit_card = CreditCard(
    "XXXX-2222",
    customer,
    50000
)


while True:

    print("\n================================")
    print("          BANKING MENU")
    print("================================")

    print("1. Account")
    print("2. Customer Services")
    print("3. Cards")
    print("4. Loans")
    print("5. Customer Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:

            print("\n----- ACCOUNT -----")
            print("1. View Account")
            print("2. Check Balance")
            print("3. Back")

            option = input("Enter choice: ")

            if option == "1":
                account.display_account()

            elif option == "2":
                account.check_balance()

            elif option == "3":
                break

            else:
                print("Invalid choice.")

    elif choice == "2":

        while True:

            print("\n----- CUSTOMER SERVICES -----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Back")

            option = input("Enter choice: ")

            if option == "1":

                amount = float(
                    input("Enter deposit amount: ₹")
                )

                account.deposit(amount)

            elif option == "2":

                amount = float(
                    input("Enter withdrawal amount: ₹")
                )

                account.withdraw(amount)

            elif option == "3":

                account.check_balance()

            elif option == "4":
                break

            else:
                print("Invalid choice.")

    elif choice == "3":

        while True:

            print("\n----- CARD SECTION -----")
            print("1. Debit Card")
            print("2. Credit Card")
            print("3. Back")

            option = input("Enter choice: ")

            if option == "1":
                debit_card.display_card()

            elif option == "2":
                credit_card.display_card()

            elif option == "3":
                break

            else:
                print("Invalid choice.")

    elif choice == "4":

        while True:

            print("\n----- LOAN SECTION -----")
            print("1. Gold Loan")
            print("2. Car Loan")
            print("3. Home Loan")
            print("4. Back")

            option = input("Enter choice: ")

            if option == "1":

                amount = float(
                    input("Enter Gold Loan amount: ₹")
                )

                loan = GoldLoan(
                    customer,
                    account,
                    amount
                )

                loan.calculate_loan()

            elif option == "2":

                amount = float(
                    input("Enter Car Loan amount: ₹")
                )

                loan = CarLoan(
                    customer,
                    account,
                    amount
                )

                loan.calculate_loan()

            elif option == "3":

                amount = float(
                    input("Enter Home Loan amount: ₹")
                )

                loan = HomeLoan(
                    customer,
                    account,
                    amount
                )

                loan.calculate_loan()

            elif option == "4":
                break

            else:
                print("Invalid choice.")

    elif choice == "5":

        customer.display_customer()

    elif choice == "6":

        print("\nThank you for using our Banking System.")
        break

    else:

        print("Invalid choice.")