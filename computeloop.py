# The formula is summation of n/n+1

numList = 100

sum = 0
n = 0.0
while n <= numList:
    sum = sum + (float)(n/(n+1))
    n += 1
print sum