#!/usr/bin/env python3
user_input = input ("Give me a number: ")
try:
    num_float =float(user_input)
    if num_float.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
                print()