#   function decaration
def add_tag(tag, word):
    output = '<'+ tag + '> ' + word + ' </' + tag + '>'
    return output

#main Program
mTag = raw_input('Please enter the tag: ')
mWord = raw_input('Please enter he word: ')

print add_tag(mTag, mWord)
