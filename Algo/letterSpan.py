# Given the passage of text, find the largest word letter span
# Word letter span defined as:
# - The distance in the alphabet between the first and the last letters of the word

# Order of the letters in the alphabet does not matter
# Capitalization does not matter
# Punctuation connected to the end of a word should be ignored
# Words with only 1 letter have a word span of 0
# Words that begin and end with the same letter have a word span of 0

# Examples

# - “wood” → "w" to "d" = abs(-19) = 19
# - “would” → "w" to "d" = 19 
# - “I” → "I" to "I" = 0
# - “dead” → "d" to "d" = 0

# Output from this process should be the span, and the list of word(s) that have that span

from collections import defaultdict


sentence = 'I would trade two wood for a sheep but not three wood.'

# Expect: 19, ["would", "wood"] or 19, ["wood", "would"] 
punctuations = [',','.','!','?',':',';']

def findLargestSpan(sentence):
    sentenceList = sentence.split()
    distances = defaultdict(list) # {0:['I','J']}
    for word in sentenceList:
        word = word.lower() 
        if word[len(word)-1] in punctuations:
            word = word[:len(word)-1]

        distance = getDistance(word)
        
        if distance in distances:
            if word not in distances[distance]:
                distances[distance].append(word)
        else:
            distances[distance] = [word]

    maxDistance = max(distances.keys())
    return distances[maxDistance]



def getDistance(word):
    firstLetter = word[0]
    lastLetter = word[len(word)-1]

    if lastLetter in punctuations:
        word = word[:len(word)-1]

    if len(word) <= 1:
        return 0
    
    if firstLetter == lastLetter:
        return 0
    
    return abs(ord(firstLetter)-ord(lastLetter))
    

print(findLargestSpan(sentence))