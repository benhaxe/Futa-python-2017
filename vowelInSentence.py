user_input = raw_input("Enter word: ")
user_lower = user_input.lower()

user_list = list(user_lower)
for i in user_list:
    if i == 'a' or i == 'e' or i == 'o' or i == 'u':
        print "The vowels are: ", i