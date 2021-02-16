import numpy


def showVowels(word):
    vowels = numpy.array(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
    new_word = ''
    for ch in word:
        if ch in vowels:
            new_word += ch
        elif ch == ' ':
            new_word += ch
        else:
            new_word += '_'
    return new_word


def checkLetter(word, ch):
    if len(ch) > 1:
        if ch.lower() == word.lower():
            return "Guessed Correctly!"
        return "Enter only one character"
    if numpy.char.isalpha(ch) != True:
        return "Enter an alphabet only"
    for i in word:
        if ch.lower() == i.lower():
            return True
    return "Wrong Guess"


def showLetter(word, ch, new_word):
    count = 0
    for i in word:
        count += 1
        if ch == i.lower():
            new_word = new_word[:count-1] + i + new_word[count:]
    return new_word
