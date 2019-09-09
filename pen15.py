import re
import string
import random 

#take out words in the dictionary that do not start with the letters in the box
#check to see if the current word is a substring of a possible word to cut on time

class TrieNode: 
    def __init__(self, parent): 
        self.parent = parent
        self.children = [None] *26 
        self.isWord = False 
#        if parent is not None: 
#            parent.children[ord(value)-97] = self


#future feature to add the count to each of the nodes aka substrings
def loadWords(fn): 
    words = open(fn)
    root = TrieNode(None)
    for word in words: 
        #check to see if the beginning of the word is even possible
        word = word[:-1]
        print(word + str(len(word)))
        if word[0] not in wordsInGrid: 
            print('skipping')
            continue

        current = root
        for letter in word.lower():
            print('before ' + str(letter))
#            if 97 <= ord(letter) < 123: 
            nextLetter = current.children[ord(letter) - 97]
            if nextLetter is None:
                nextLetter = TrieNode(current)
            current = nextLetter
        current.isWord = True         
        print('\n\n')
    return root
       
#get lower case letters only
letters = string.ascii_letters[:26]


#populate the grid
box = []
for i in range(0,4): 
    row = []
    for j in range(0,4): 
        row.append(random.choice(letters))
    box.append(row)
    row= []


#get the possible characters in the grid
stringifyRow = []
for row in box: 
   stringifyRow.append(''.join(row))

wordsInGrid = ''.join(set(''.join(stringifyRow)))
print(wordsInGrid)

wordsInGrid = 'hjmdimpte'
dictionary = loadWords('test.txt')

