# Fibonacci Sequence

# Define the initial values of the sequence
x = 0
y = 1


user_input = int(input("How many numbers would you like to be generated? "))
# Number of Fibonacci numbers to generate
n = user_input

# Initialize a list to store the Fibonacci numbers
fibonacci_sequence = []

# Generate the Fibonacci sequence
for _ in range(n):
    fibonacci_sequence.append(x)
    x, y = y, x + y

# Print the Fibonacci sequence
print("Fibonacci Sequence:")
for number in fibonacci_sequence:
    print(number)
