def mergeSort(arr, arr2, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow
        # for large l and h
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, l, m)
        mergeSort(arr, arr2, m + 1, r)
        mergeSortMerge(arr, arr2, l, m, r)

def mergeSortMerge(arr, arr2, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        j += 1
        k += 1 

def merge(year, month, day):
    try:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        line_int = ""
        line_int += year
        month_str = str(months.index(month) + 1)
        if len(month_str) == 1:
            month_str = "0" + month_str
        line_int += month_str
        line_int += day
        return(int(line_int))
    except:
        return 0

def isMatch(word):
    pass

filename = "wordle.dat"
fh = open(filename, "r")

lines = fh.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

words = []
dates = []
for line in lines:
    month, day, year, word = line.split()
    myDate = merge(year, month, day)
    dates.append(myDate)
    words.append(word)

mergeSort(words, dates, 0, len(words) - 1)

print("Welcome to the Wordle Database!")
valid = False
userOption = ""
while not valid:
    userOption = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if userOption.lower() == "w":
        valid = True
    elif userOption.lower() == "d":
        valid = True

if userOption == "w":
    valid = False
    while not valid:
        userInput = input("What word are you looking for? ")
        if len(userInput) == 5:
            valid = True
elif userOption == "d":
    valid = False
    while not valid:
        year = input("Enter the year: ")
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day = input("Enter the day: ")
        date = merge(year, month, day)
        if date != 0:
            valid = True
        