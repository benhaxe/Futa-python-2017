#   Harmonic mean
#   When ever you see the symbol summation note that you will use the for and range

#   Task: ... blahblahblah

k = input("Please, enter the value for k: ")
sum = 0.0
for n in range(1, k+1):
    x = ((-1)**(n+1))/n
    sum = sum + x
print "sum = ", sum