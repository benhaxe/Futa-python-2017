var1 = raw_input("Enter your name to determine numeric value: ")

var1_lower = var1.lower()

to_name_list = list(var1_lower)

numericOfVar1 = 0
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in to_name_list:
    numericOfVar1 += alphabet.index(i)
print "Your name is: ", var1
print "Numeric Value is: ", numericOfVar1
