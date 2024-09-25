# Predict
# I predict that when running the code and inputting C, it will output "I prefer cherries". If you enter any other letter, symbol, or number, it will also output "I prefer cherries"
# since if you follow the if statments, it is not "A" and it is not "B" so it will result in the else printing "I prefer cherries".
# This is a problem because it is not the choice that the user input or wanted

# Modify 1
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):
    print("I prefer cherries")
else:
    print("Unexpected input")

# You can also improve this further by making it not matter if the user input a capital or lower letter:
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch.upper() == "A"):
    print("I prefer apples")
elif (ch.upper() == "B"):
    print("I prefer bananas")
elif (ch.upper() == "C"):
    print("I prefer cherries")
else:
    print("Unexpected input")

# Modify 2:
number = int(input("Enter a number from 1-100: "))
if (number >= 80) and (number <= 100):
  print("A")
elif (number >= 70) and (number <= 79):
  print("B")
elif (number >= 60) and (number <= 69):
  print("C")
elif (number >= 50) and (number <= 59):
  print("D")
elif (number >= 1) and (number <= 50):
  print("F")
else:
  print("Invalid number")
