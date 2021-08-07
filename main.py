# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Exercise 3: Given a string, display only those characters which are present at an even index number.
# extra: try print a word and get rid of the vowels
# Orginal String is  pynative
# Printing only even index chars: p n t v



letters = input("Please enter a string variable: ")
# function to split the letter of the string
def split(word):
    return [char for char in word]
separate = split(letters)
#i=0 #No need to initialise.
for i in range(len(separate)):
    if not i%2 : #same as i%2 ==o , 0 is false 1 is true
        print(separate[i])
        #i = +1
#my code seems to freak out when I want to join the characters to form a string
#how can I refer to print the corresponding indext of the character
# print('\n\n')
# word_str = 'pynative'
# vowels = ['a','e','i','o','u','','','']
# word  = split(word_str)
# i = 0
# for i in range(len(word)):
#     if(vowels[i] != word[i]):
#         print(word[i])
#         i += 1
# word = input("enter a string: ")
word = "pynative"
vow = 'a', 'o', 'u', 'i', 'e'

for i in range(8):
    vowflg = False

    for j in range(5):
        if word[i] == vow[j]:
            vowflg = True

    if not vowflg:
        print(word[i])

# for i in range(len(word)):
#     if not i%2:
#         print(word[i])

# for letter in word:
#     vowflg=False

#     for vowel in vowels:
#         if letter==vowel:
#             vowflg=True

#     if not vowflg:
#         print(letter)

# vows = "aeiou"
# for letter in word:
#     if not letter in vows:
#         print(letter)