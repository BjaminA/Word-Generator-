
WordGen2: Advanced Random Word Generator
Description
WordGen2 is a sophisticated Python script for generating random words with a unique twist. It combines the simplicity of randomly choosing syllables with the complexity of using statistically weighted consonants. This script offers three different methods for word generation, each providing a distinct style of word construction.

Features
Three Word Generation Methods: Pattern-based, Initial Consonant-based, and Statistically Biased Consonant-based.
Statistical Weighting: Utilises a frequency dictionary built from a sample word list to weight the selection of consonants.
Customisable Word Length: Users can specify the desired length for the generated word.
Syllable-based Construction: Incorporates a predefined list of syllables for word creation.
How It Works
Frequency Dictionary: The script first builds a frequency dictionary of consonants from a list of sample words to understand the commonality of each consonant.
Word Generation Methods:
Pattern-Based: Alternates between 2-letter and 3-letter syllables.
Initial Consonant-Based: Starts with a consonant, followed by syllables. For longer words, an additional consonant is inserted in the middle.
Statistically Biased Consonant-Based: Begins with a statistically biased consonant and follows the pattern of the Initial Consonant-Based method.
Random Selection: Syllables and consonants are randomly selected, with consonant selection influenced by their frequency in the sample word list.
Output: The script displays the generated words from each method.
Usage
Run the Script: Execute the script in a Python environment.
Enter Word Length: Input the desired length of the word when prompted.
View Results: The script will display the generated words from each method.
Example
Mathematica
Copy code
Input: 7
Output:
Pattern-Based Word: "ogreake"
Word with Initial Consonant: "treaump"
Statistically Biased Word: "neashon"
Requirements
Python 3.x
Collections module for Counter (usually included in standard Python distribution).
Limitations
The words generated may not always be meaningful or commonly used.
The script relies on a predefined list of syllables and a sample word list for consonant frequency, which may not cover all linguistic possibilities.
Customisation
Users can expand the list of sample words or syllables to alter the output.
The non_randomness_factor can be adjusted to control the influence of consonant frequency on word generation
