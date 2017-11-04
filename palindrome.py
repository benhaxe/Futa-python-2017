word=str(raw_input("enter the word:"))
y=list(word)
a=""
for j in range(len(word)-1,-1,-1):
               a = a+y[j]
if (a==word):
    print"palindrome"
else:
    print"not palindrome"
