import random
import string
from collections import Counter

# Expanded sample words list
sample_words = [
    "example", "word", "list", "to", "create", "frequency", "dictionary", "cat", "dog", "apple", "orange", "tree", "book", "river", "mountain", "cloud", "sky",
"rain", "sun", "moon", "star", "planet", "ocean", "beach", "sand", "rock", "hill",
"valley", "forest", "garden", "flower", "leaf", "branch", "root", "seed", "bird", "fish",
"insect", "animal", "human", "child", "adult", "person", "friend", "family", "team", "group",
"city", "town", "village", "country", "nation", "world", "space", "universe", "galaxy", "system",
"light", "dark", "color", "sound", "smell", "taste", "touch", "sight", "feeling", "thought",
"idea", "dream", "goal", "plan", "action", "effort", "work", "play", "game", "sport",
"music", "song", "dance", "art", "painting", "picture", "photo", "camera", "phone", "computer",
"car", "train", "plane", "ship", "boat", "bike", "road", "path", "journey", "trip",
"school", "class", "lesson", "teacher", "student", "book", "paper", "pen", "study", "knowledge"
]

# Define vowels and consonants
vowels = ('a', 'e', 'i', 'o', 'u')
alphabet = list(string.ascii_lowercase)
consonants = list(set(alphabet) - set(vowels))

def buildFrequencyDict(words):
    """Builds a frequency dictionary for consonants from the given list of words."""
    all_consonants = ''.join([char for word in words for char in word if char in consonants])
    frequency_dict = Counter(all_consonants)
    return frequency_dict

def weightedRandomConsonant(frequency_dict, non_randomness_factor):
    """Selects a consonant based on weighted frequency, adjusted by a factor."""
    if non_randomness_factor <= 0:
        return random.choice(consonants)
    
    weighted_consonants = []
    for consonant, freq in frequency_dict.items():
        weighted_consonants.extend([consonant] * int(freq ** non_randomness_factor))
    
    return random.choice(weighted_consonants if weighted_consonants else consonants)

# Define a list of syllables
syllables = ["og", "ide", "ie", "re", "mem", "ber", "ake", "sh", "ch", "on", "ain", "ump", 
             "ree", "ee", "oat", "ould", "ob", "ug", "oor", "le", "el", "ake", "pa", "ph", 
             "one", "ass", "an", "ere", "en", "wh", "civ", "il", "al", "ant"]

def generatePatternBasedWord(wordLength):
    """Generates a word using a combination of 2-letter and 3-letter syllables."""
    word = ""
    syllable_order = [2, 3]  # Alternating pattern of syllable lengths
    current_length = 0

    while current_length < wordLength:
        syllable_length = syllable_order[current_length % 2]
        if current_length + syllable_length > wordLength:
            break
        syllable = random.choice([syl for syl in syllables if len(syl) == syllable_length])
        word += syllable
        current_length += syllable_length

    return word

def generateWordWithInitialConsonant(wordLength):
    """Generates a word starting with a consonant, followed by 2 or 3-letter syllables."""
    word = random.choice(consonants)  # Start with a consonant
    current_length = 1  # Current word length

    while current_length < wordLength:
        if wordLength >= 8 and (current_length == 3 or current_length == 4):
            word += random.choice(consonants)  # Add a middle consonant
            current_length += 1
        else:
            syllable_length = 3 if current_length + 3 <= wordLength else 2
            syllable = random.choice([syl for syl in syllables if len(syl) == syllable_length])
            word += syllable
            current_length += syllable_length

    return word

def generateStatisticallyBiasedWord(wordLength, freq_dict, non_randomness_factor):
    """Generates a word using syllables and statistically biased consonants."""
    word = weightedRandomConsonant(freq_dict, non_randomness_factor)  # Start with a biased consonant
    current_length = 1  # Current word length

    while current_length < wordLength:
        # Decide on syllable length based on remaining length in word
        syllable_length = 3 if current_length + 3 <= wordLength else 2
        syllable = random.choice([syl for syl in syllables if len(syl) == syllable_length])

        # Add syllable to word
        word += syllable
        current_length += syllable_length

        # Insert a statistically biased consonant in the middle for longer words
        if wordLength >= 8 and (current_length == 3 or current_length == 4):
            word += weightedRandomConsonant(freq_dict, non_randomness_factor)
            current_length += 1

        # Ensure not to exceed word length
        if current_length >= wordLength:
            break

    return word


def main():
    """Main function to demonstrate word generation."""
    wordLength = int(input("Enter the desired word length: "))
    freq_dict = buildFrequencyDict(sample_words)
    non_randomness_factor = 2.0  # Adjust this value to influence randomness

    patternWord = generatePatternBasedWord(wordLength)
    initialConsonantWord = generateWordWithInitialConsonant(wordLength)
    statisticallyBiasedWord = generateStatisticallyBiasedWord(wordLength, freq_dict, non_randomness_factor)

    print("Pattern-Based Word:", patternWord)
    print("Word with Initial Consonant:", initialConsonantWord)
    print("Statistically Biased Word:", statisticallyBiasedWord)

main()
