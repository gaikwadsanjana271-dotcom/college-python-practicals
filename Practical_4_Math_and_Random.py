# Practical No. 4
# Aim: Demonstrate Python math and random modules

import math
import random

def basic_math_operations():
    num1 = 16
    num2 = 4

    print("Basic Math Operations:")
    print(f"Square root of {num1}: {math.sqrt(num1)}")
    print(f"{num1} raised to the power of {num2}: {math.pow(num1, num2)}")
    print(f"Sine of {num1} degrees: {math.sin(math.radians(num1)):.4f}")
    print(f"Cosine of {num2} degrees: {math.cos(math.radians(num2)):.4f}")
    print(f"Factorial of {num2}: {math.factorial(num2)}")

def random_number_operations():
    print("\nRandom Number Operations:")
    print("Random float between 0 and 1:", random.random())
    print("Random integer between 10 and 50:", random.randint(10, 50))
    print("Random choice from a list:", random.choice([2, 4, 6, 8, 10]))

    random_list = [1, 2, 3, 4, 5]
    random.shuffle(random_list)
    print("Shuffled list:", random_list)
    print("Random sample of 3 elements from the list:", random.sample(random_list, 3))

if __name__ == "__main__":
    basic_math_operations()
    random_number_operations()
