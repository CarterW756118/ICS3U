# 1
n = int(input("Input a value: "))
fac = n
count = n
while (count > 0):
  count -= 1
  if (count != 0):
    fac *= count
print("%d! = %d" % (n, fac))

# 2
n = int(input("Input a value: "))
n_count = 1
while (n_count <= n):
  fac = n_count
  count = n_count
  while (count > 0):
    count -= 1
    if (count != 0):
      fac *= count
  print("%d! = %d" % (n_count, fac))
  n_count += 1

# 3
n = int(input("Input a value: "))
n_count = 0
while (n_count <= n):
  fac = n_count
  count = n_count
  while (count > 0):
    count -= 1
    if (count != 0):
      fac *= count
  if (n_count == 0):
    fac = 1
  print("%d! = %d" % (n_count, fac))
  n_count += 1
