#   Task: write a python program containing a function called fibonacci from 1 to any given position
#   assuming that your position is 4 then the fibonacci is fibonacci of the first 6 numbers

# the function fibonacci
def fibonacci(n):
    #   let a and b be first and second value respectively
    #   and n is the position given by the user
    a = 1
    b = 1
    print a
    print b
    final_pos = n + 1
    for j in range(a, final_pos):
        c = a + b
        print c
        a = b
        b = c
    return c

# Main Body
user_position = input("Enter a given position of your choice: ")
fibonacci(user_position)

#   Explanation
#   in fibonacci the first and second number starts from 1
#   at line 12 c will be t
#   at line 14 the new value of a will be the initial value of b
#   and the new value of b will be the value c
#   a and b are declared outside the function so that they can later be updated.