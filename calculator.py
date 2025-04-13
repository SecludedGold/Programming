#simple calculator

import math

def add(num1,num2):
    add=num1+num2
    print(add)

def multiply(num1,num2):
    multiply=num1*num2
    print(multiply)

def subtract(num1,num2):
    subtract=num1-num2
    print(subtract)

def divide(num1,num2):
    divide=num1/num2
    print(divide)
    
def powers(num1,num2):
    powers=num1**num2
    print(powers)

def root(num1):
    root=math.sqrt(num1)
    print(root)


num1 = 0
num2 = 0

running=True
while running:
    function=input("add, multiply, subtract, divide, powers, root, or quit: ")
    function=function.lower()
    if function in ["add", "multiply", "subtract", "divide", "powers"]:
        num1=int(input("Input a number: "))
        num2=int(input("Input another number: "))
    if function == "add":
        add(num1,num2)
    elif function == "multiply":
        multiply(num1,num2)
    elif function == "subtract":
        subtract(num1,num2)
    elif function == "divide":
        divide(num1,num2)
    elif function == "powers":
        powers(num1,num2)
    elif function == "root":
        num1=int(input("Input a number to be rooted: "))
        root(num1)
    else:
        running=False