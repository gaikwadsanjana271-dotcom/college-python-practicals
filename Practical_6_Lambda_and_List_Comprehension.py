# Practical No. 6
# Aim: Demonstrate lambda functions and list comprehension

numbers = [1, 2, 3, 4, 5]

# Lambda with map() to find squares
squares = list(map(lambda x: x ** 2, numbers))

# Lambda with filter() to find even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list:", numbers)
print("Squares using lambda:", squares)
print("Even numbers using lambda:", evens)

# List comprehension
squares_lc = [x ** 2 for x in numbers]
evens_lc = [x for x in numbers if x % 2 == 0]

print("Squares using list comprehension:", squares_lc)
print("Evens using list comprehension:", evens_lc)
