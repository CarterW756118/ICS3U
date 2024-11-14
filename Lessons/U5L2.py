filename = "C://Users/Carter/Downloads/smiley_emoji_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()
colorData = colorData.replace('"', '').replace(',', '')
rows, cols, numColors = colorData.split()

rows = int(rows)
cols = int(cols)
numColors = int(numColors)

colorDefs = []
for i in range(numColors):
    colorLine = fh.readline() 
    colorLine = colorLine.strip()
    colorLine = colorLine.replace('"', '').replace(',', '')
    sym, c, color = colorLine.split()
    if sym == '~':
        sym = " "
    colorDefs.append([sym, color])

imageData = []
for i in range(rows):
    row = fh.readline()
    row = row.strip()
    row = row.replace('"', '').replace(',', '')
    rowArr = []
    for j in range(len(row)):
        color = row[j]
        for k in range(numColors):
            if color == colorDefs[k][0]:
                color = colorDefs[k][1]
        rowArr.append(color)
    imageData.append(rowArr)

print("Dimensions: %d x %d" % (rows, cols))
print("Number of colors:", numColors)
print("Colors:", colorDefs)
for i in imageData:
    print(i)

fh.close()