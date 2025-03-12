# String Palindrome without slicing 
name = input("Enter your name: ")
is_palindrome = True
for i in range(len(name) // 2):
    if name[i] != name[-i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")