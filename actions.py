import pandas
from random import randint

try:
    data = pandas.read_csv('./data/words_to_learn.csv').to_dict()
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv').to_dict()
finally:
    french_words = [value for (key, value) in data['French'].items()]
    english_words = [value for (key, value) in data['English'].items()]


def choose_random_words():
    random_num = randint(0, len(french_words) - 1)
    return [french_words[random_num], english_words[random_num]]


def i_know_this_word(french_word, english_word):
    french_words.remove(french_word)
    english_words.remove(english_word)

    new_words = {
        'French': french_words,
        'English': english_words
    }

    pandas.DataFrame(new_words).to_csv('./data/words_to_learn.csv')




