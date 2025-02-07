# to take input from the user use input built-in functions in python

name = input("Enter your name: ")

print("Hello", name," 👋")

# to check the current working directory

import os
print(os.getcwd())

# to change the current working directory

os.chdir("C:\\Users\\merns\\Desktop")

print(os.getcwd())

# to get the current system time

import datetime
print(datetime.datetime.now())

# to generate a random number

import random
print(random.randint(1, 100))