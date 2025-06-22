print("Enter the first number.")
first_number = input()
print("Enter second number.")
second_number = input()
product = int(first_number) * int(second_number)
print(first_number,"x",second_number,"=",product)

if int(product) == 0:
    print("The result is zero.")
if int(product) > 0 :
    print("The result is positive.")
if int(product) < 0 :
    print("The result is negatiive.")
