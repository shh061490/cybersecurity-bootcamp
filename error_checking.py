
while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"You entered the number: {number}")
        break
    except ValueError:
        print("That's not a valid number. Try again.")