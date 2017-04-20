# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When no argument is provided print out
# No source provided
# When the argument provided and the source is a file
# count all words in the given file and print the most common
# ("cat", "CAT", "cat," "cat." are different words )

import sys

def print_description():
    print("usage: python most_common_word.py [source]")

def warning_message():
    print("No source provided")

def count_words(file_name):
    try:
        text = open(file_name , "r")
        words_to_count = text.read()
        num_of_words = 0
        text.close()

    except FileNotFoundError:
            return 0


def controller(arg):
    if len(sys.argv) == 1:
        warning_message()
    else:
        print_description()

controller(sys.argv)
