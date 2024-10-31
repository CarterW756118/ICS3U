import random

def shuffle(A):
    for i in range(len(A)):
        temp = A[i]
        j = random.randint(0, len(A) - 1)
        A[i] = A[j]
        A[j] = temp
    return A
    
size = 6
B = []
for i in range(1, size + 1):
    B.append(i)

print(B) # before
B = shuffle(B)
print(B) # after
