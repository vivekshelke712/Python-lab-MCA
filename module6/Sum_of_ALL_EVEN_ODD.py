def sum_even_odd(n):
    sum_even = sum(i for i in range(2, n + 1, 2))
    sum_odd = sum(i for i in range(1, n + 1, 2))
    return sum_even, sum_odd

def main():
    n = int(input("Enter a number: "))
    sum_even, sum_odd = sum_even_odd(n)
    print(f"Sum of even numbers up to {n}: {sum_even}")
    print(f"Sum of odd numbers up to {n}: {sum_odd}")

if __name__ == "__main__":
    main()
