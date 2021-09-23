"""""
*author - Manish Singh
*date 20-09-2021
*time - 05:55 PM
*Title - Quadratic
"""""

import math


class Quadratic:
    root1 = 0
    root2 = 0

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    determinant = b * b - 4 * a * c
    if determinant > 0:
        root1 = (-b + math.sqrt(determinant)) / (2 * a)
        root2 = (-b - math.sqrt(determinant)) / (2 * a)
        print(root1, root2)
    elif determinant == 0:
        root1 = root2 = -b / (2 * a)
        print(root1)
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-determinant) / (2 * a)
        print("root1 = ", real,"and", imaginary)
        print("root2 = ", real,"and", imaginary)