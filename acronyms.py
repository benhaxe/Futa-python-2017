input_phrase = raw_input("Please enter your phrase here: ")
# the join function takes in 2 parameter the self and iterable
acronym = "".join(i[0] for i in input_phrase.split())
newAcronym = acronym.upper()
print newAcronym