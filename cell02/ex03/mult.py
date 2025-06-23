#!/usr/bin/env python3
print("Enter the first number.")
number_1 = input()
print("Enter second number")
number_2= input()
product = int(number_1) * int(number_2)
print(number_1,"x",number_2,"=",product)

if int(product) == 0:
    print("The result is zero.")
if int(product) > 0 :
    print("The result is positive.")
if int(product) < 0 :
    print("The result is negatiive.")
