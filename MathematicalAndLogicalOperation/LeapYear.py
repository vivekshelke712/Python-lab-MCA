year = int(input("Enter a Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

num = int(input("Enter a number: "))
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

num2 = int(input("Enter another number: "))
if num2 % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
