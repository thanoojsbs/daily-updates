1. Student Grade Calculator
name = input("Enter student name: ")

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
average = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")



2. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Choose operation: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")


3. Number Guessing Game
import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("You won!")
else:
    print("You lost!")
    print("Correct number was:", secret)