#!/usr/bin/env python
import random
import sys
from sys import argv


script, filename = argv


d = {}
def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # read our text file into a variable
    f = open(corpus, "r")
    myfile = f.read()
    f.close()
    # split that string into single words
    word_list = []
    word_list = myfile.split()

    # use a for loop to create tuples to be the keys in the dictionary
    d = {}
    for i in range(len(word_list)-2):
        word_1 = word_list[i]
        word_2 = word_list[i + 1]
        word_3 = word_list[i + 2]
        # if the tuple word_1, word_2 exists in the dictionary, append word_3 to the values
        if d.get((word_1, word_2)):
            d[word_1, word_2].append(word_3)
        # if the tuple word_1, word_2 does not exist in the dictionary, add it and set the va
        # to word_3
        else:
            d[word_1, word_2] = [word_3]
    return d

d = make_chains(filename)

print d

def make_tuple(dictionary):
    #generate the keys of the dictionary as a list
    list_of_keys = dictionary.keys()
    # select a random number on the range of the length of the list
    random_tuple = random.choice(list_of_keys)
    # print the item at that index in the list_of_keys
    return random_tuple




def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # start a sentence with two words (a tuple)
    # start with capital letter or capital letter following a quotation mark
    # end with ".", "?", "!", or one of those followed by a quotation mark 
    start_bigram = make_tuple(chains)
    text_string = []
    text_string.append(start_bigram[0])
    text_string.append(start_bigram[1])

    for i in range(6):

        first_word = text_string[i]
        second_word = text_string[i + 1]
            # look up the start bigram in the dictionary
            # add a random item from its associated values to the end 
        text_string.append(random.choice(chains[first_word, second_word]))
    return text_string



    # go look up that tuple in the dictionary
    # return the a random item from the value (which is a list) 
    # associated with the tuple
    # do the same thing with the new last two words
    #return "Here's some random text."

def main():
    args = sys.argv

    #Change this to read input_text from a file
    input_text = filename

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()