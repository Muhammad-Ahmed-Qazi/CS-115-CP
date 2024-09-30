user_input = input("Enter an integer: (N/n to exit)\n>>> ")

if user_input not in "Nn":
    greatest = int(user_input)

    while user_input not in "Nn":
        if int(user_input) > greatest:
            greatest = int(user_input) 
        user_input = input("Enter an integer: (N/n to exit)\n>>> ")

    print("Largest integer in the inputs:", greatest)