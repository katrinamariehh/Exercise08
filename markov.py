#!/usr/bin/env python
import random
import sys
from sys import argv


script, filename = argv


chains = {}
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
    #this will delete quotation marks from the beginning and end of word in the list
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip('"')

    # use a for loop to create tuples to be the keys in the dictionary
    chains = {}
    for i in range(len(word_list)-2):
        word_1 = word_list[i]
        word_2 = word_list[i + 1]
        word_3 = word_list[i + 2]
        # if the tuple word_1, word_2 exists in the dictionary, append word_3 to the values
        if chains.get((word_1, word_2)):
            chains[word_1, word_2].append(word_3)
        # if the tuple word_1, word_2 does not exist in the dictionary, add it and set the va
        # to word_3
        else:
            chains[word_1, word_2] = [word_3]
    return chains

chains = make_chains(filename)

# print chains

def make_tuple(dictionary):
    # generate the keys of the dictionary as a list
    list_of_keys = dictionary.keys()
    # narrow down the list of keys to capital_letter_keys and 
    # include only those that start with a capital letter
    capital_letter_keys = []
    for item in list_of_keys:
        # if the first character of the first item in the tuple is a capital letter
        # and the last character of the first item is a lower-case letter
        first_letter = item[0][0]
        last_letter = item[0][-1]
        if ord(first_letter) >= 65 and ord(first_letter) <= 90 and ord(last_letter) >=97 and ord(last_letter) <=122:
            # add it to the list of capital_letter_keys
            capital_letter_keys.append(item)
    # select a random item from the list of keys that start with at capital letter
    random_tuple = random.choice(capital_letter_keys)
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
    end_characters = ['.', '?', '!', '"', '!"', '?"', '."']
    # while the last character of the last item of the list is not in the 
    # end_character list, keep lopping
    while text_string[-1][-1] not in end_characters:
        first_word = text_string[-2]
        second_word = text_string[-1]
            # look up the start bigram in the dictionary
            # add a random item from its associated values to the end 
        text_string.append(random.choice(chains[first_word, second_word]))
    text_string = ' '.join(text_string)
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