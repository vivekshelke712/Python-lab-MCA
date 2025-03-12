# Print Common Char in Two String
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
common_chars = set(name1) & set(name2)
print(f"Common characters in {name1} and {name2}: {', '.join(common_chars)}")
