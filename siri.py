import re
import string
import random 

#take out words in the dictionary that do not start with the letters in the box
#check to see if the current word is a substring of a possible word to cut on time

class TrieNode: 
    def __init__(self, parent, value): 
        self.parent = parent
        #this should not be hardcoded : should be able to include symbols etc... 
        self.children = [None] *26 
        self.isWord = False 
        self.count = 0 
        #added this for debugging, tho not needed
        self.value = value
#        if parent is not None: 
#            parent.children[ord(value)-97] = self


#recursive implementation 
def rec(root, word):
    if(len(word) == 0):
        return
    charnum = ord(word[0]) - ord('a')
    node = None
    #if the letter already exists there, move to it
    if(root.children[charnum] != None):
        node = root.children[charnum]
    #if the letter does not exist there, create it and move to it
    else:
        node = TrieNode(root, word[0])
        root.children[charnum] = node
    #increment the count of that substring regardless
    root.count += 1
    if(len(word) == 1):
        node.isWord = True
    else:
        rec(node, word[1:])


#future feature to add the count to each of the nodes aka substrings
#iterative implementation but reused for loading words
def loadWords(fn): 
    words = open(fn)
    root = TrieNode(None, None)
    for word in words: 
        #check to see if the beginning of the word is even possible
        word = word.lower()
        word = word.strip()
        if word[0] not in wordsInGrid:
            print(str(word) + ' does not begin with one of the letters in the grid')
            continue
        print(word) 
        rec(root, word)
    for i in range(25):
        if root.children[i] != None :
            print("%c: %d" %  (chr(i + ord('a')), root.children[i].count ))
    return root



def findWords(box, dictionary):
    print('finding words')
    #validWords = [] 
    validWords = set()
    firstLetters = []

    for row in range(len(box)):
        for column in range(len(box[0])):
            firstLetter = box[row][column]
            firstLetterNode = dictionary.children[ord(firstLetter) - ord('a')]        
            #added this for testing purposes 
            if firstLetterNode is not None:
                visitedGrid = []
                for c in range(len(box)):
                    rowFalse = []
                    for r in range(len(box[0])): 
                        rowFalse.append(False)
                    visitedGrid.append(rowFalse)
                firstLetters.append((column, row, firstLetterNode, firstLetterNode.value, visitedGrid))

    print('hi mom')
    #add 3 or more letters 
    #add non repeating characters
    while firstLetters: 
        x, y, currentNode, currentLetter, visited = firstLetters[0]
        print('next up in the queue: ') 
        print('first element:  ', x,y,currentLetter)
        for a, b, c, d, e in firstLetters: 
            print(str(a) + ',' + str(b) + ' :' + str(d) + '; ' , end =" ")
        visited[y][x] = True
        print(visited)

        del firstLetters[0]

        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)): 
            x2 = dx + x
            y2 = dy + y

            
            if 0 <= x2 < len(box[0]) and 0 <= y2 < len(box): 
                if visited[y2][x2] is True: 
                    continue
                nextLetter = box[y2][x2]
                substring = currentLetter + nextLetter 
                print('around ' + str(x) + ', ' + str(y) + ' : ' + str(x2) + ', ' + str(y2) + ' is ' + nextLetter + '= ' + substring)
                nextLetterNode = currentNode.children[ord(nextLetter) - ord('a')]
                if nextLetterNode is not None: 
                    print('potential substring : ' + substring)
                    if nextLetterNode.isWord and len(substring) >= 3: 
                        print('valid substring: ' + substring)
                        #we can add to a set if we want the unique substrings in the grid, or a regular list if we want all of the substrings including duplicates
                        validWords.add(substring)
                        #validWords.append(substring)                        
                    #only add it to the queue if the next possible word is in the dictionary
                    firstLetters.append((x2, y2, nextLetterNode, substring, visited))
    return validWords

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

#box = [['h', 'i', 't', 'd'], ['t', 'e', 's', 'l'], ['h', 'j', 'm', 'a'], ['p', 't', 'e', 's']]
print(box)
#get the possible characters in the grid
stringifyRow = []
for row in box: 
   stringifyRow.append(''.join(row))

wordsInGrid = ''.join(set(''.join(stringifyRow)))
print(wordsInGrid)

#wordsInGrid = 'hjmdmpte'
#dictionary = loadWords('test.txt')
dictionary = loadWords('./google-10000-english/20k.txt')


#search for words : 
wordsFound = findWords(box, dictionary)
print(wordsFound)
