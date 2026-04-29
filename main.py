import transaction

def show_menu():
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Exit")


def run_atm():
    print("Welcome to Our ATM Service!")
    transaction_history=[]

    while True:
        show_menu()
        choice = int(input("Enter Number from the menu according to your need: "))

        if choice == 1:
            print(f"Your Account Balance is {transaction.check_balance()}")
        
        elif choice == 2:
            amt=int(input("Enter the amount to Deposite: "))
            if transaction.deposit(amt):
                print(f"{amt} is Deposited Succesfully. Your current Balance is {transaction.check_balance()}") 
                transaction_history.append(f"{amt} deposit")
            else :
                print("Earn Some Money! You Looser!")

        elif choice == 3:
            amt=int(input("Enter the amount to Withdraw: "))
            if transaction.withdraw(amt):
                print(f"Withdraw succesful {amt} is in your hand. Use it wisely.")
                transaction_history.append(f"{amt} withdraw")
            else:
                print("Earn some money to withdraw from you account! NOOB!")
        
        elif choice == 4:
            print("\n--- YOUR MINI STATEMENT ---")
            if not transaction_history:
                print("No transactions recorded yet.")
            else:
                for entry in transaction_history:
                    print(f" - {entry}")
            print("---------------------------")

        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Are you blind!")
run_atm()