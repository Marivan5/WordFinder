import re

file = open("words.txt", "r")

listOfWords = file.read()
listOfWords = listOfWords.split("\n")

print("Number of words: " + str(len(listOfWords)))

loop = "y"

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

while loop == "y":
    print("Type some letters: ", end="")

    inputWord = input()
    print("")

    if(inputWord == ""):
        inputWord = "ormagnide"

    lettersRegex = re.compile(r"^[" + inputWord + "]*$")

    words = []
    longestWord = ""

    for word in listOfWords:
        if(lettersRegex.match(word)):
            words.append(word)

    for word in words:
        for i in inputWord:
            if(word.count(i) > inputWord.count(i)):
                words = remove_values_from_list(words, word)

    words.sort(key = len)

    for word in words:
        if(len(word) > len(longestWord) and len(word) <= len(inputWord)):
            longestWord = word;
        print(word)

    print("The longest Word is: " + longestWord)

    print("Total amount of words found: " + str(len(words) - 1))

    print("Do you want to try again? (y/n): ", end="")
    loop = input()