while True:
    try:
        print("0 Exit\n1 Calculator \n2 To be continue \n")
        write = input("What do you want: ")
        write_word = write.lower()
    # find Exit
        Exit_first_letter = write.find("e")
        Exit_last_letter = write.find("t")
        find_Exit = write_word[Exit_first_letter:(Exit_last_letter + 1)]
    # find Calculator
        Calculator_first_letter = write_word.find("c")
        Calculator_last_letter = write_word.find("r")
        find_Calculator = write_word[Calculator_first_letter:(Calculator_last_letter + 1)]
    # find Continue
        Continue_first_letter = write_word.find("c")
        Continue_last_letter = write_word.find("e")
        find_Continue = write_word[Continue_first_letter:(Continue_last_letter + 1)]

        if find_Exit == "exit" or write == "0":
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            print("Okay, bye")
            break
        elif find_Calculator == "calculator" or write == "1":

            # Calculator
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            number1 = float(input("Write the first number: "))
            number2 = float(input("Write the second number: "))
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            print("1: addition \n2: subtraction \n3: division \n4: multiplication \n")
            write_operator = input("Select operation: ")
            word = write_operator.lower()
            result = "Error in solution"
            # find Addition
            Addition_first_letter = write_operator.find("a")
            Addition_last_letter = write_operator.find("n")
            find_Addition = word[Addition_first_letter:(Addition_last_letter + 1)]
            # find Subtraction
            Subtraction_first_letter = write_operator.find("s")
            Subtraction_last_letter = write_operator.find("n")
            find_Subtraction = word[Subtraction_first_letter:(Subtraction_last_letter + 1)]
            # find Division
            Division_first_letter = write_operator.find("d")
            Division_last_letter = write_operator.find("n")
            find_Division = word[Division_first_letter:(Division_last_letter + 1)]
            # find Multiplication
            Multiplication_first_letter = write_operator.find("m")
            Multiplication_last_letter = write_operator.find("n")
            find_Multiplication = word[Multiplication_first_letter:(Multiplication_last_letter + 1)]

            if find_Addition == "addition" or write_operator == "1" or write_operator == "+":
                result = number1 + number2
            elif find_Subtraction == "subtraction" or write_operator == "2" or write_operator == "-":
                result = number1 - number2
            elif find_Division == "division" or write_operator == "3" or write_operator == "/":
                result = number1 / number2
            elif find_Multiplication == "multiplication" or write_operator == "4" or write_operator == "*":
                result = number1 * number2
            else:
                print("┏◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚┓")
                print(" You write something wrong.")
                print(" TIP: Try the whole word or choose one of the numbers")
                print("┗◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛┛")
                continue
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            print(result)
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")

        elif find_Continue == "continue" or write == "2":
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            print("There's nothing here yet")
            print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
            continue
        else:
            print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
            print(" Error. You write something wrong or nothing was written")
            print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")

# Possible Errors
    except ZeroDivisionError:
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
        print(" You can't divide zero")
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
    except ValueError:
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
        print(" Error. You write something wrong or nothing was written")
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
    except Exception as result:
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
        print( f"Something went wrong: {result}")
        print("|◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢|")
