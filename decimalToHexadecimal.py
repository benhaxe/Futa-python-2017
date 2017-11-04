def ChangeToHex(n):
    if(n < 0):
        print (0)
    elif(n <= 1):
        print n,
    else:
        ChangeToHex(n / 16)
        x = (n % 16)
        if (x < 10):
            print(x),
        if (x == 10):
            print ("A"),
        if (x == 11):
            print ("B"),
        if (x == 12):
            print ("C"),
        if (x == 13):
            print ("D"),
        if (x == 14):
            print ("E"),
        if (x == 15):
            print ("F"),
        if (x > 15):
            print ("The number is greater than hexadecimal")

#   Main body
#   user_input is the argument that is passed into the function
user_input = input("please input an integer: ")
ChangeToHex(user_input)