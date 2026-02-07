# Question 1
n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print("Sum from 1 to", n, "=", total)


# Question 2

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial of", n, "=", fact)
