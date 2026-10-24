# Practical: Lambda Functions and List Comprehensions

# Part 1: Squares and even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = lambda x: x * x

squares = [square(x) for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)

# Part 2: Add a 10% bonus to salaries and filter salaries over 50000
print()
salaries = [30000, 45000, 50000, 60000, 75000]

add_bonus = lambda salary: salary + (salary * 10 / 100)

updated_salaries = [add_bonus(salary) for salary in salaries]
high_salaries = [salary for salary in updated_salaries if salary > 50000]

print("Original Salaries:", salaries)
print("Salaries After 10% Bonus:", updated_salaries)
print("Salaries Greater Than 50000:", high_salaries)
