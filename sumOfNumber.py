def countingNumbers(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

def oddNumbers(n):
    sum = 0
    i = 1
    while i <= (2*n) - 1:
        if (i%2)== 1:
            sum += i
        i += 1
    return sum

def evenNumbers(n):
    sum = 0
    i = 1
    while i <= n:
        if (i%2)== 0:
            sum += i
        i += 1
    return sum

    return ()

# main body
b = int(raw_input("end: "))
print "The sum of all numbers from 1 to ", b, "is: ", countingNumbers(b)
print "The sum of all odd numbers from 1 to ", (2*b)-1, "is: ", oddNumbers(b)
print "The sum of all even numbers from 1 to ", b, "is: ", evenNumbers(b)