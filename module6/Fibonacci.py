# Write a function to Display the Fibonacci Sequences up to nth Term Where n is Provided by the user. 

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
    
fibonacci(10)