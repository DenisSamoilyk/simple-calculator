try:
    number1 = int(input("Write the first number:"))
    number2 = int(input("Write the second number:"))
    print("\n1 addition \n2 subtraction \n3 division \n4 multiplication")
    operator = int(input("Select operation:"))
    if operator == 1:
        result = number1 + number2
    elif operator == 2:
        result = number1 - number2
    elif operator == 3:
        result = number1 / number2
    elif operator == 4:
        result = number1 * number2
    else:
        print("Wrong operator")
    print(result)
# Possible Errors
except ZeroDivisionError:
    print("You can't divide zero")
except ValueError:
    print("Error. You can only write numbers or nothing was written")
except Exception:
    print("Something went wrong")
