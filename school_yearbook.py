"""
Author : Carter Wells
Student Number: 756118
Revison date : 23 October 2024
Program : School Yearbook
Description : A program that computes the minimum area and dimensions for photos with 
    1x1 units being placed in a yearbook.
VARIABLE DICTIONARY :
    done (bool) = Boolean value of if the user has entered done and if the loop should keep running
    valid (bool) = Boolean value of if the user has entered valid input
    num_photos (int) = Number of photos the user has input
    user_input (str) = User input for the amount of photos or "done"
    user_input_int (int) = The input amount of photos converted to int
    factors (list) = List of factors a number has
    max_num (int) = Max factor
    x (int) = X value of the dimensions
    y (int) = Y value of the dimensions
    perimeter (int) = The perimeter of the photos
"""

import math

def factor(N):
    factors = []
    max_num = math.floor(math.sqrt(N))
    for x in range(1, max_num + 1):
        if N % x == 0:
            factors.append(x)
    return factors

def min_perimeter(N):
    factors = factor(N)
    x = max(factors)
    y = N / x
    perimeter = 2 * (x + y)
    print("Minimum perimeter is %d with demensions of %d x %d" % (perimeter, x, y))

print("Welcome to the school yearbook program!")
done = False
while not done:
    valid = False
    num_photos = 0
    while not valid:
        user_input = input("Please input your number of photograpghs: ")
        if user_input.lower() == "done":
            valid = True
            done = True
            print("Goodbye!")
            exit()
        try:
            user_input_int = int(user_input)
            if user_input_int > 0:
                valid = True
                num_photos = user_input_int
            else:
                print("%d is not a valid number of photos." % user_input_int)
        except:
            print("%s is not a valid number of photos." % user_input)
    min_perimeter(num_photos)
            
    
