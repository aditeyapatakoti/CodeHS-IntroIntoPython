initial_balance = 1000
user_choice = input("Would you like to make a deposit or would you like to withdrawal? Please type deposit for a deposit and withdrawal for a withdrawal: ")

if user_choice == "withdrawal":
    withdraw_amount = int(input("How much money would you like to withdraw?"))
    if withdraw_amount >1000:
        print("You cannot have a negative balance")
    else:
        initial_balance = initial_balance - withdraw_amount
    print("Final balance:", str(initial_balance))
elif user_choice == "deposit":
    deposit_amount = int(input("How much money would you like to deposit?"))
    initial_balance = initial_balance + deposit_amount
    print("Final balance:", str(initial_balance))
else:
    print("Invalid transaction")
