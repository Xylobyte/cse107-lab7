"""
A program that takes a string and counts the ocurrances of letters in it

file: lettercount.py

author: Donovan Griego

Date: 10-10-2021

assignment: Lab 7
"""


def main():
    # Gets input and calls the function to get a sorted dictionary
    letters = dict(sorted(count_letters(
        input("Enter some letters >>> ")).items()))
    for key in letters.keys():
        print(key, letters[key])


def count_letters(string):
    """
    returns a dictionary with letters found in the string and their counts

    string: string to count letters
    """
    # Cleaning up string of spaces and lowers it
    string = string.lower().replace(" ", "")
    letters = {}
    for l in string:
        # If letter is in dictionary add 1 to it, else add an entry of 1
        if l in letters.keys():
            letters[l] += 1
        else:
            letters[l] = 1
    return letters


if __name__ == "__main__":
    main()
