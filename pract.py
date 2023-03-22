
# i=0
# while (i<=1000):
#     i=i+1
#     print(i)
#
for x in range(1,1000,2):
    print(x," ")
# speed = 45
# SPEED_LIMIT = 50
# turbo = True
# if speed < SPEED_LIMIT:
#     speed = speed + 10
# elif speed < SPEED_LIMIT and turbo:
#     speed = speed + 25
# print(speed)
#
# i = 1
# while i < 11:
#     i = i + 1
# print(i)
#
# total = 0
# for i in range(0, 2):
#     for j in range(0, 2):
#         for k in range(0, 3):
#             total = total + 1
# print(total)
#
# nums = [2, 1, 0]
# names = ["Ada", "Babbage", "Cookie"]
# print([nums[2]])
#
#
#
# import numpy as np
# a = np.array([ [1, 2, 3, 4], [5, 6, 7,8], [4, 7, 9, 7]])
# print(a.size)
#
# a = np.array([ [-5, 7], [3, -4]])
# print(a[a > 0])
#
# def FunctionFour(N):
#     if N <= 1:
#         return 1
#     return 2*FunctionFour(N-1)
# n=FunctionFour(2)
# print(n)
#
# def getNegs(L):
#     result = []
#     for num in L:
#         if not num > 0:
#             result.append(num)
#     return result
#
# for i in range(2,1001,2):
#     print(i)
#
# def power2(N):
#     if N == 0:
#         return 1
#     else:
#         return 2 * power2(N-1)

x = 100
if x < 1000:
    x=5
elif x <= 5:
    x = 17
if x < 6:
    x=4
else:
    x = 101

print(x)

midterm = "zjiokfafcihug"
print(midterm[len(midterm):0:-1])

greeting="PIKA"
print('"'+greeting+'"')
a = 15
b = 4
c = 0
x = 2.5
y = 2.0
z = 0.0
print(not (a <= b) and (b < x) or (y + z) > a)



arr = ["Would", "you", "like", "to", "buy", "an", "O?"]
n = arr[0]
c = arr[-1]
for i in range(len(arr)):
    arr[i] = c
    c = n
    p = i + 1
    if (p >= len(arr)):
        p = 0
        n = arr[p]

print(arr[0])

total = 0
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 3):
            total = total + 1
print(total)

L = []
for i in range(4):
    L.append([i])
print(L)

def message():
    m = "pika!"
    return m
m=message()
print(m)

import numpy as np
def pengiunSightings(map, r, c):
    if r < 0 or r > 24 or c < 0 or c > 24:
        return -1
    region = map[max(0, r-1):min(r+1,24)+1, max(0,c-1):min(c+1,24)+1]
    return np.sum(region)
q=pengiunSightings(20,25,30)
print(q)
