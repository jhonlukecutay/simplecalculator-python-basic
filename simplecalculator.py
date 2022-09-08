from ast import Break, If


print("Calculator Program")
print("")


def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y



while True:
    usernum1 = int(input("Please add the first number: "))
    usernum2 = int(input("Please add the second number: "))

    print("The number you'll pick has designated arithmetic function below.")
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")


    arith = input("Please pick a number between 1 to 4: ")

    if arith == '1':
        print(usernum1, "+", usernum2, "=", addition(usernum1, usernum2))
    elif arith == '2':
        print(usernum1, "-", usernum2, "=", subtraction(usernum1, usernum2))
    elif arith == '3':
        print(usernum1, "X", usernum2, "=", multiplication(usernum1, usernum2))
    elif arith == '4':
        print(usernum1, "/", usernum2, "=", division(usernum1, usernum2))
    
    nxt_calcu = input("Would you like to use this again? y/n: ")
    
    if nxt_calcu == "N":
        break
    else:
        continue

else:
    print("invalid input.")
    