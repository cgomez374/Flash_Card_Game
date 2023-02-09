import pandas
from random import randint

# Read from saved data (words_to_learn) or start from the beginning (french_Words)

try:
    data = pandas.read_csv('./data/words_to_learn.csv').to_dict()
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv').to_dict()
finally:
    french_words = [value for (key, value) in data['French'].items()]
    english_words = [value for (key, value) in data['English'].items()]


# Chooses random English and French words from both lists
def choose_random_words():
    random_num = randint(0, len(french_words) - 1)
    return [french_words[random_num], english_words[random_num]]


# Removes the known word from both lists and saves new list to WORDS_TO_LEARN
def i_know_this_word(french_word, english_word):
    french_words.remove(french_word)
    english_words.remove(english_word)

    new_words = {
        'French': french_words,
        'English': english_words
    }

    pandas.DataFrame(new_words).to_csv('./data/words_to_learn.csv')




