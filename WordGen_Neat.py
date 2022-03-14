from pickle import APPEND
import string
from stringprep import in_table_c5
import math
import random

def calculateRatios(wordLength): 
    vowlCount = math.ceil(wordLength/2) 
    constCount = wordLength - vowlCount
    print("number of vowl is " + str(vowlCount))
    print("number of const is " + str(constCount))
    return([vowlCount,constCount])

def selectLetters(numberToSelect,letters):
    selectedLetters = []
    for i in range(numberToSelect):
        selectedLetters.append(random.choice(letters))
    return selectedLetters

def generateWord(vowels,constants):
    combined = list(zip(vowels,constants)) # <-- zip combines two lists
    ##looks like [('a','g'),('e','z'),...] <-- we want to remove the tuples and combine the list into one string
    print(combined)
    print (len(vowels))
    x = len(vowels) - 1 
    if len(vowels) % 2 != 2:
        combined.append(vowels[x])
    generatedWord = []
    for tup in combined: # for each tuple
        for letter in tup: # for each letter 
            generatedWord.append(letter) # now looks like ['a','g','e',...] so just need to combine into one string

    return "".join(generatedWord) #return "age..."

def main():
    ## all letters
    alphabet=list(string.ascii_lowercase)

    ## vowels
    vowels=('a','e','i','o','u')

    ## constants
    constants = list(set(alphabet) - set(vowels))
    
    ## word length
    wordLength = int(input("How long should the word be?"))
    
    ## number of vowels/constants
    vowelCount, constantCount = calculateRatios(wordLength)

    ##randomly selected vowels/constants
    generatedVowels = selectLetters(vowelCount,vowels)
    generatedConstants = selectLetters(constantCount,constants)

    ##print vowel/consts which will be used
    print("generated vowels: " + str(generatedVowels))
    print("generated consts: " + str(generatedConstants))

    ##generate word
    generatedWord = generateWord(generatedVowels,generatedConstants)
    GendWord2 = GenWord2(generatedVowels,generatedConstants, wordLength)
    print("Generated word is: " + generatedWord)

    print(GendWord2)



# run main
main()
