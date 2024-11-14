filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()
colorData = colorData.replace('"', '')
colorData = colorData.replace(',', '')
rows, cols, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

colorDefs = []
for i in range(numColors):
    colorLine = fh.readline() 
    colorLine = colorLine.strip()
    colorLine = colorLine.replace('"', '')
    colorLine = colorLine.replace(',', '')
    sym, c, color = colorLine.split()
    if sym == '~':
        sym = " "
    colorArr = []
    colorArr.append(sym)
    colorArr.append(color)
    colorDefs.append(colorArr)

print("Dimensions: %d x %d" % (rows, cols))
print("Colors:", colorDefs)

fh.close()