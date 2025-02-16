# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:37:38 2025

@author: iizit
"""

import math

def basic_operations():
    print("Basic Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")

def scientific_operations():
    print("Scientific Operations:")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    print("8. Arcsine (asin)")
    print("9. Arccosine (acos)")
    print("10. Arctangent (atan)")
    print("11. Square (x²)")
    print("12. Square Root (√)")
#created a ui to test the code
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
#added a if statmint to make sure ther are no errors
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def arcsine(x):
    if -1 <= x <= 1:
        return math.degrees(math.asin(x))
    else:
        return "Error! Input out of range."

def arccosine(x):
    if -1 <= x <= 1:
        return math.degrees(math.acos(x))
    else:
        return "Error! Input out of range."
#added a if statmint to make sure ther are no errors again
def arctangent(x):
    return math.degrees(math.atan(x))

def square(x):
    return x ** 2

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot calculate the square root of a negative number."
#used the math module for most functions to save time
def calculator():
    while True:
        print("\nChoose an operation:")
        print("1. Basic Operations")
        print("2. Scientific Operations")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            basic_operations()
            op = input("Choose operation (1/2/3/4): ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == '1':
                print(f"Result: {add(num1, num2)}")
            elif op == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif op == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif op == '4':
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid Input")

        elif choice == '2':
            scientific_operations()
            op = input("Choose operation (5-12): ")
            num = float(input("Enter number: "))

            if op == '5':
                print(f"Result: {sine(num)}")
            elif op == '6':
                print(f"Result: {cosine(num)}")
            elif op == '7':
                print(f"Result: {tangent(num)}")
            elif op == '8':
                print(f"Result: {arcsine(num)}")
            elif op == '9':
                print(f"Result: {arccosine(num)}")
            elif op == '10':
                print(f"Result: {arctangent(num)}")
            elif op == '11':
                print(f"Result: {square(num)}")
            elif op == '12':
                print(f"Result: {square_root(num)}")
            else:
                print("Invalid Input")

        elif choice == '3':
            print("Exiting the calculator...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    calculator()
#combleted the ui code to test the functions 