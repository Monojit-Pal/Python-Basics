#WAF to print the factorial of n

n = int(input("Enter n : "))

def factorial(n):
    fact = 1
    for idx in range(1, n+1):
        fact *= idx
    return fact

print("Factorial :", factorial(n))