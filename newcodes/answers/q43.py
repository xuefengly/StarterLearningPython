#!/usr/bin/env python
# coding=utf-8

import random

number = random.randint(1,100)
guess = 0

while True:
    num_input = input("please input one integer that is in 1 to 100:")
    guess += 1
                
    if not num_input.isdigit():
        print("Please input interger.")
    elif int(num_input) < 0 or int(num_input) >= 100:
        print("The number should be in 1 to 100.")
    else:
        if number == int(num_input):
            print("OK, you are good. It is only {0}, then you successed the number is {1}.".format(guess, num_input))
            break
        elif number > int(num_input):
            print("your number is smaller.")
        elif number < int(num_input):
            print("your number is bigger.")
