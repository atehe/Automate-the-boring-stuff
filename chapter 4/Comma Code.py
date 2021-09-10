
def comma_code(list_val):
    list_str=''
    for word in list_val:
        if word == list_val[0]:
            list_str += word
        elif word == list_val[-1]:
            list_str += ' and ' + word
        else:
            list_str += ', ' + word
    return list_str



spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))

