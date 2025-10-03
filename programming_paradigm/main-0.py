import sys
from bank_account import BankAccount

def main():
    # Default initial balance is 0, but can be set via command line
    initial_balance = 0
    if len(sys.argv) > 1:
        try:
            initial_balance = float(sys.argv[1])
        except ValueError:
            print("Invalid initial balance. Using $0.00.")
    account = BankAccount(initial_balance)

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            amount = input("Enter amount to deposit: ").strip()
            try:
                amount = float(amount)
                if account.deposit(amount):
                    print(f"Deposited ${amount:.2f}")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            amount = input("Enter amount to withdraw: ").strip()
            try:
                amount = float(amount)
                if account.withdraw(amount):
                    print(f"Withdrew ${amount:.2f}")
                else:
                    print("Insufficient funds or invalid amount.")
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
