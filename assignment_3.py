import turtle            # should be at the top of your code
turtle.bgcolor("gray40") # dark gray - try gray70 for a lighter gray
turtle.tracer(0,0)       # turns off updates to speed up plotting
t = turtle.Turtle()      # makes it easier to call the plotting functions

def modify(ln):
    mod_string = ""
    badChars = ['"', ',']
    ln = ln.strip()
    for c in ln:
        if c not in badChars:
            mod_string = mod_string + c
    return mod_string

def plotIt(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

def drawImage(img, pixel_size, rows, cols):
    x_half = int(-cols / 2)
    y_half = int(-rows / 2)
    for x in range(len(imageData)):
        y_half += 1
        for y in range(len(imageData[x])):
            plotIt(t, x_half * pixel_size, -y_half * pixel_size, pixel_size, imageData[x][y])
            x_half += 1
        x_half = int(cols / 2) * -1

filename = "rocky_bullwinkle_mod.xpm"
fh = open(filename, "r")

t.hideturtle() # prevents the plotter sprite from appearing in your image

colorData = fh.readline()
colorData = modify(colorData)
rows, cols, numColors = (0,0,0)
try:
    rows, cols, numColors = colorData.split()
except:
    rows, cols, numColors, temp = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

colorDefs = []
for i in range(numColors):
    colorLine = fh.readline() 
    colorLine = modify(colorLine)
    sym, c, color = colorLine.split()
    if sym == '~':
        sym = " "
    colorDefs.append([sym, color])

imageData = []
for i in range(rows):
    row = fh.readline()
    row = modify(row)
    rowArr = []
    for j in range(len(row)):
        color = row[j]
        for k in range(numColors):
            if color == colorDefs[k][0]:
                color = colorDefs[k][1]
        rowArr.append(color)
    imageData.append(rowArr)

fh.close()

print("Dimensions: %d x %d" % (rows, cols))
print("Number of colors:", numColors)
print("Colors:", colorDefs)
drawImage(imageData, 4, rows, cols)
