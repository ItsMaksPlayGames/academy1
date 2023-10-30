# try except

#
# try:
#     number = int(input("Enter number "))
#     print(10 / number)
# except:
#     print("we have some error !")
# # 2
# try:
#     number = int(input("Enter number "))
#     print(10 / number)
# except ValueError as ex:
#     print("we have some ValueError - ", ex)
#
# # 3
# try:
#     number = int(input("Enter number "))
#     print(10 / number)
# except ValueError as ex:
#     print("we have some ValueError - ", ex)
# except ZeroDivisionError as ex:
#     print("Error -", ex)
#
# # 4
# try:
#     number = int(input("Enter number "))
#     print(10 / number)
# except (ValueError, TypeError) as ex:
#     print("we have some - ", ex)
# except ZeroDivisionError as ex:
#     print("Error -", ex)
# else:
#    print("finished code ok")
#
# finally:
#     print("try ended")


def checkType(value):
    if type(value) == str:
        return value
    elif type(value) == int:
        raise TypeError("we need str and int got instead!")
    else:
        raise TypeError

try:
    checkType(123)
except TypeError as ex:
    print("An error occurred:", ex)


while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Please choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")


        choice = input("Your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please try again.")
            continue

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2

        print("Result:", result)
    except ValueError as ex:
        print("Input error:", ex)



