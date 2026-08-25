# main.py

from utils import square, is_even, celsius_to_fahrenheit, greet

number = float(input("Enter a number: "))
name = input("Enter your name: ")

print("Square:", square(number))
print("Even or Odd:", "Even" if is_even(number) else "Odd")
print("Fahrenheit:", celsius_to_fahrenheit(number))
print(greet(name))