# Predict
"""
Prediction A:
Python
Prediction B:
P
Prediction C:
Python
D:
The purpose of setting sep and end to "" is so that there will be no spaces between letters and so that it will print each letter on the same line instead of the default new line (\n)
E:
The purpose of the empty print statement is so that the cursor will move to the next line
Prediction F:
0 P
1 y
2 t
3 h
4 o
5 n
"""

# Modify
progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
spaces = 0
for c in progname:
  if c == " ":
    spaces += 1
print("There are %d spaces in the text." % spaces)
