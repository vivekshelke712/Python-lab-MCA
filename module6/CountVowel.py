def count_vcb(s):
    v = "aeiouAEIOU"
    c = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    v_count = 0
    c_count = 0
    b_count = 0

    for ch in s:
        if ch in v:
            v_count += 1
        elif ch in c:
            c_count += 1
        elif ch == " ":
            b_count += 1

    return v_count, c_count, b_count

# Example usage:
s = "Hello World! How are you?"
v, c, b = count_vcb(s)

print("Vowels:", v)
print("Consonants:", c)
print("Blanks:", b)
