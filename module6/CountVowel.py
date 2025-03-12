# count vowel in the String
name = input("Enter your name: ")
vowels = "aeiouAEIOU"
count = 0
for char in name:
    if char in vowels:
        count += 1
print(f"Number of vowels in {name}: {count}")

