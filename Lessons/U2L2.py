# Predict
# a) I would expect that it would output (After asking for the two numbers):
# Now deciding if 3 is a factor of 6 ...
# Yes! 3 is a factor of 6
# This is because you are asked to input whole number values for x and y and it checks if the remainer of the the two numbers being divided is equal to 0, if it is then y is a factor of x.
# b) I would expact that it would output (After asking for the two numbers):
# Now deciding if 5 is a factor of 6 ...
# It only outputs that and not it is a factor because the remainder of x and y is not equal to 0 and therefore y is not a factor of x

# Run
# I was correct with my prediction

# Modify
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)

# Modify 2
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
  print("You are not allowed to enter zero, and a factor could not be determined")

# Modify 3
import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if (x >= 1 and x <= 20):
  y = input("Please input another whole number between 1 and 20: ")
  y = int(y)
  if (y >= 1 and y <= 20):
    rem = x % y
    if rem == 0:
      print("Yes!", y, "is a factor of", x)
    else:
      print("No!", y, "is not a factor of", x)
  else:
    print(y, "is outside of range. Cannot continue.")
  
else:
  print(x, "is outside of range. Cannot continue.")
