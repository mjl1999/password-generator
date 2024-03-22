from random import shuffle
from secrets import choice
from string import ascii_letters, punctuation, digits
import time
print("Welcome to random Py Password Generator!")

password = ""

time.sleep(1)
letters = int(input("How many letters would you like in your password: "))
for i in range(letters):
    password += choice(ascii_letters)

time.sleep(1)
numbers = int(input("How many numbers would you like in your password: "))
for i in range(numbers):
    password += choice(digits)

time.sleep(1)
symbols = int(input("How many symbols would you like in your password: "))
for i in range(symbols):
    password += choice(punctuation)

password_list = list(password)
shuffle(password_list)
while not password_list[0].isalpha():
    shuffle(password_list)

final_password = ''.join(password_list)

time.sleep(1)
print(f"Suggested password: {final_password}")
