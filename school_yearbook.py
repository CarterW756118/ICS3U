import math

def factor(N):
    factors = []
    max_num = math.floor(math.sqrt(N))
    for x in range(1, max_num + 1):
        if N % x == 0:
            factors.append(x)
    return factors

def min_perimeter(N):
    factors = factor(N)
    y = N / x

print("Welcome to the school yearbook program!")
done = False
while not done:
    valid = False
    num_photos = 0
    while not valid:
        user_input = input("Please input your number of photograpghs: ")
        if user_input.lower() == "done":
            valid = True
            done = True
            print("Goodbye!")
            break
        try:
            user_input_int = int(user_input)
            if user_input_int > 0:
                valid = True
                num_photos = user_input_int
            else:
                print("%d is not a valid number of photos." % user_input_int)
        except:
            print("%s is not a valid number of photos." % user_input)
            
    
