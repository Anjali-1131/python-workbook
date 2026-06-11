# CREATE A CALCULATOR FUNCTION
# def calculator(a, b, operation):
#     try:
#         calculation = { 
#             "+" : (a+b), 
#             "-" : (a-b), 
#             "/" : (a/b), 
#             "*" : (a*b)
#             }
#         return calculation[operation]
#     except KeyError as kyerr:
#         print(kyerr)
#         print("Please Enter a Valid key!")

def calculator(a, b, operation):
    calculation = { 
        "+" : (a+b), 
        "-" : (a-b), 
        "/" : (a/b), 
        "*" : (a*b)
        }
    return calculation.get(operation, "Please enter a valid operation!")
    
firstNumber = int(input("Enter the 1st Number:"))
secondNumber = int(input("Enter the 2nd Number:"))
task = input("Enter the Operation which you want to be performed:")

print(calculator(firstNumber, secondNumber, task))


'''def calculator(a, b, operation):
    if operation == "+":
        return (a+b)
    if operation == "-":
        return (a-b)
    if operation == "/":
        return (a/b)
    if operation == "*":
        return (a*b)
    
firstNumber = int(input("Enter the 1st Number:"))
secondNumber = int(input("Enter the 2nd Number:"))

task = input("Enter the Operation which you want to be performed:")

calculator(firstNumber, secondNumber, task) '''