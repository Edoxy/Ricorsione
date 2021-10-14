import time

def Hanoi(n, start, finish, count):
    #n = number of layers
    #start = from 1 to 3 the star position of the tower
    #finish = from 1 to 3 the finish posision of the tower
    other = 6 - (start + finish)

    if n == 1:
        count = step(start, finish, count)
    else:
        count = Hanoi(n-1,start, other, count)
        count = step(start, finish, count)
        count = Hanoi(n-1, other, finish, count)
    return count
def step(start, finish, count):
    #print(start, '->', finish)
    count += 1
    return count
n = 25
start = 1
finish = 3
count = 0

count = Hanoi(n, start, finish, count)
print(count)
