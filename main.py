from movieDetails import *
from checkLetter import *

def guessMovie():
    attempts = 9
    print(f"Guess the movie name ({attempts} attempts).")
    movie = getMovieDetails()
    movieToGuess = showVowels(movie[0])
    print(movieToGuess)
    wrongCount = 0
    while movieToGuess != movie[0] and wrongCount != 10:
        ch = input('Enter guess: ')
        letterInName = checkLetter(movie[0], ch)
        if letterInName == "Guessed Correctly!":
            return letterInName
        elif letterInName != True:
            wrongCount += 1
            print(f'{letterInName} ({attempts - wrongCount} attempts left)')
            if wrongCount == 4:
                print(f'Hint: Year of release - {movie[1]}')
            if wrongCount == 7:
                print(f'''Hint: Actor - {movie[2]}, Actress - {movie[3]}''')
            print(movieToGuess)
        else:
            movieToGuess = showLetter(movie[0], ch, movieToGuess)
            print(movieToGuess)
    if wrongCount == 10:
        return "Better luck next time!"
    else:
        return "Guessed correctly!"


print(guessMovie())