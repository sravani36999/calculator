def add(a, b):
    return a + b 

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b 

def div(a, b):
    if b == 0:
        return "Cannot divided by Zero"
    else:
        return a/b 


print("Simple Calculator")
print("Choose Operation: ")
print("'+' for Addition")
print("'-' for substraction")
print("'*' for Multiplication")
print("'/' for Division")

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number: "))

operator = input("Enter a operator: ")

if operator == "+":
    print("Result: " , add(num1,num2))
elif operator == "-":
    print("Result:",sub(num1,num2))
elif operator == "*":
    print("Result:",mul(num1,num2))
elif operator == "/":
    print("Result:",div(num1,num2))
else:
    print("Invalid Operator")


'''Interview explanation for this project

“I built a Calculator Application using Python. 
It takes two numbers and an operator from the user 
and performs addition, subtraction, multiplication, 
or division using functions and conditional statements. 
I also handled division by zero using a condition.”'''
