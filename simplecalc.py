#simple calculator

#init
#functions
#this function adds num1 + num2 and prints the result
def add(num1, num2):
    sum = num1 + num2
    print("The sum is: " + str(sum))
def sub(num1, num2):
    ans = num1 - num2
    print("The answer is: " + str(ans))
def mult(num1, num2):
    ans = num1 * num2
    print("The answer is: " + str(ans))
def div(num1, num2):
    ans = num1 / num2
    print("The answe is: " +str(ans))
def Simple_Calculator():
    print("Welcome Preschoolers to Simple Calculator") #welcome statement
    while True:
        print("Please choose an operation: ") #user choice input
        print("""1.Addition
        2.Subtraction
        3.Multiplication
        4.Division
        5.Quit""") #various kinds of operations
        operation = int(input("(1-5) :"))

        if operation == 1:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            add(add1, add2)
        if operation == 2:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            sub(add1, add2)
        if operation == 3:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            mult(add1, add2)
        if operation == 4:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            sub(add1, add2)
        if operation == 5: #break function to end the while true 
            print("Goodbye")
            break

#main
Simple_Calculator()
