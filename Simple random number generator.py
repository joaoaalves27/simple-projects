import random

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

random_number = random.randint(start, end)

print(f"A random number between {start} and {end} is: {random_number}")