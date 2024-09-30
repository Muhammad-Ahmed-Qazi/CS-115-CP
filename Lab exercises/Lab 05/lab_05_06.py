user_id = input("Enter your ID: ")

counter = 0
consent = "Y"
while consent in "Yy":
    counter += 1
    print("\nMain Menu\n" + "*" * 11)
    print("1. Deposit Money\n2. Withdraw Amount\n3. Login as a Different User")
    choice = int(input("Select your choice ... "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        print(f"${amount} has been deposited to your account.")
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        print(f"${amount} has been withdrawn from your account.")
    elif choice == 3:
        user_id = input("Enter your new ID: ")
        print(f"Logged in as user {user_id}.")
    else:
        print("Invalid choice. Please try again.")
        continue   

    if counter != 2:
        consent = input("\nDo you want to continue? [y/Y] ")
    else: consent = " "

