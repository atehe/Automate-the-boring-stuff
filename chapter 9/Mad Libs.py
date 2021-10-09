



text ='The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'


text_list = text.split(' ')

occurence = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for word in occurence:
    if word in text_list:
        
        text_list.replace(word,)

# for word in text_list:
#     if word == 'ADJECTIVE':
#         word = input('Enter an adjective:')
#     elif word == 'NOUN':
#         word = input('Enter a noun:')
#     elif word == 'VERB':
#         word =input('Enter a verb:')
#     elif word == 'noun':
#         word = input('Enter a noun:')
    


madlib = ' '.join(text_list)

print(madlib)
