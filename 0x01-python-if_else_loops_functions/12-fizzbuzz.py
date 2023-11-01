#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", sep=' ', end='')
            continue
        elif num % 3 == 0:
            print("Fizz", sep=' ', end='')
            continue
        elif num % 5 == 0:
            print("Buzz", sep=' ',  end='')
        print(num, sep=' ', end='')
