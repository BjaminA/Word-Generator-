# Word-Generator-


WordGen1: Random Word Generator
Description
WordGen1 is a Python script designed to create random words based on a specified length. The script generates words by combining vowels and consonants in a balanced manner. It ensures the word is composed of approximately half vowels and half consonants, based on the length of the word specified by the user.

Features
User-specified Word Length: The script allows users to input the desired length for the word.
Balanced Mix of Vowels and Consonants: It calculates the number of vowels and consonants based on the word length, aiming for a 50/50 distribution.
Random Letter Selection: Vowels and consonants are randomly selected to construct the word.
How It Works
Word Length Input: The script prompts the user to enter the desired word length.
Calculating Ratios: It calculates the number of vowels and consonants needed. The number of vowels is approximately half the word length (rounded down), and the remaining letters are consonants.
Selecting Letters: Randomly selects the calculated number of vowels and consonants from the English alphabet.
Word Construction: The script then alternates between the selected vowels and consonants to construct the word. If the numbers of vowels and consonants are unequal, the excess letters are added to the end of the word.
Output: The generated word is displayed.
Usage
Run the Script: Execute the script in a Python environment.
Enter Word Length: Input the desired length of the word when prompted.
View the Result: The script will display the generated word.
Example
vbnet
Copy code
Input: 5
Output: Generated word is: "afero"
In this example, for a word of length 5, the script generates a word with a mix of vowels and consonants.

Requirements
Python 3.x
No additional libraries are required.
