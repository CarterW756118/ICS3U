"""
Author : Carter Wells
Student Number: 756118
Revison date : 23 October 2024
Program : School Yearbook
Description : A program that computes the minimum area and dimensions for photos with 
    1x1 units being placed in a yearbook.
VARIABLE DICTIONARY :
    done (bool) = Boolean value of if the user has entered done and if the loop should
        keep running
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

# Imports math library
import math

# Finds factors of a number and returns them as a list
def factor(N):
    # Defines empty factors list
    factors = []
    # Max num/factor, which is the rounded down value of the square root of N
    max_num = math.floor(math.sqrt(N))
    # Finds the factors of N, and appends/adds them to factors list
    for x in range(1, max_num + 1):
        # If N divided by x has no remainder, add x to the factors list
        if N % x == 0:
            factors.append(x)
    # Return factors list
    return factors

# Finds the dimensions and minimum perimeter for the number of photos
def min_perimeter(N):
    # Calls factor function and sets factors to the returned list
    factors = factor(N)
    x = 1
    # Finds the max value from the factor list
    for num in factors:
        # If num is greater then x, set x to num
        if num > x:
            x = num
    # Sets y to N divided by x
    y = N / x
    # Calculates perimeter
    perimeter = 2 * (x + y)
    # Prints perimeter and the dimensions 
    print("Minimum perimeter is %d with dimensions of %d x %d" % (perimeter, x, y))

# Prints welcome message
print("Welcome to the school yearbook program!")
done = False
# Runs while done is false (until user inputs "done")
while not done:
    # Prints a new line
    print()
    valid = False
    num_photos = 0
    # Runs until user input is considered valid
    while not valid:
        # Asks user for number of photograpghs
        user_input = input("Please input your number of photograpghs: ")
        # If the user input is "done", set done and valid to true and exit the loop
        if user_input.lower() == "done":
            valid = True
            done = True
            print("Goodbye!")
            break
        try:
            # Converts the user input into type int
            user_input_int = int(user_input)
            # If the int is greater than 0 then input is valid and num_photos is set
            if user_input_int > 0:
                valid = True
                num_photos = user_input_int
            # User input number number less than 1
            else:
                # Prints that the input is not a valid number of photos
                print("%d is not a valid number of photos." % user_input_int)
        # Runs if user_input could not be converted into int, meaning user input a string
        except:
            # Prints that the input is not a valid number of photos
            print("%s is not a valid number of photos." % user_input)
    # Calls min_perimeter function if done is false (so it does not run if user input "done" before)
    if not done:
        min_perimeter(num_photos)
            
    
