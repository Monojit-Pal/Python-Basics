import cmath

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    # Find the roots
    root1, root2 = find_roots(a, b, c)

    # Print the roots
    print(f"The roots of the quadratic equation are", root1," and", root2)