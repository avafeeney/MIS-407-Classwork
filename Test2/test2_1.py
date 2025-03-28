total = 0.0
command = ""
while command != "q":
    command = input("Enter command +, -, or q to quit: ")
    if command == "q":
        break
    elif command == "+" or "-":
        try:
            num = float(input("Enter the number to add or subtract: "))
            if command == "+":
                total += num
            elif command == "-":
                total -= num
            else:
                print("Invalid command. Please enter +, -, or q to quit.")
        except ValueError:
            print("Value entered isn't a valid number. Try again.")
    else:
        print("Invalid command. Please enter +, -, or q to quit.")

    print(f"Total is: {total}")


