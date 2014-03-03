#!/usr/bin/env python
import random
import sys
import twitter
import os
from sys import argv


script, filename, ngram = argv


chains = {}
def make_chains(corpus, ngram_length):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # read text file into a variable
    f = open(corpus, "r")
    myfile = f.read()
    f.close()
    # split text file string into single words
    word_list = []
    word_list = myfile.split()
    # delete quotation marks from the beginning and end of word in the list
    for i in range(len(word_list)):
        word_list[i] = word_list[i].strip('"')
        word_list[i] = word_list[i].strip("'")

    chains = {}
    # use a for loop to create tuples to be the keys in the dictionary
    # this for loop creates a bigram-based dictionary
    # for i in range(len(word_list)-2):
    #     word_1 = word_list[i]
    #     word_2 = word_list[i + 1]
    #     word_3 = word_list[i + 2]
    #     # if the tuple word_1, word_2 exists in the dictionary, append word_3 to the values
    #     if chains.get((word_1, word_2)):
    #         chains[word_1, word_2].append(word_3)
    #     # if the tuple word_1, word_2 does not exist in the dictionary, add it and set the va
    #     # to word_3
    #     else:
    #         chains[word_1, word_2] = [word_3]
    # attempting to add ability to select the lenth of the ngram
    # TODO a default of 2 of no length is given?

    # iterating over the word list
    for i in range(len(word_list) - int(ngram_length)):
        # iterating over the length of the ngram
        for j in range(int(ngram_length) + 1):
            ngram = []
            # each word in the ngram can be referenced as the i index plus the j index
            ngram.append(word_list[i+j])
        # but this makes ngram a list and to be a key in the dictionary it needs to be a tuple
        ngram_key = ngram[:-1]
        ngram_value = ngram[-1]
        # this looks up the ngram in the dictionary
        if chains.get(ngram_key):
            # adds the value if the ngram is already present
            chains(ngram_key).append(ngram_value)
        else:
            # and creates the initial key-value pair if the ngram is not present
            chains[ngram_key] = ngram_value

    return chains

chains = make_chains(filename, ngram)

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
        if ord(first_letter) >= ord('A') and ord(first_letter) <= ord('Z') and ord(last_letter) >= ord('a') and ord(last_letter) <= ord('z'):
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
    text_list = []
    text_list.append(start_bigram[0])
    text_list.append(start_bigram[1])
    end_characters = ['.', '?', '!', '"', '!"', '?"', '."']
    # while the last character of the last item of the list is not in the 
    # end_character list, keep lopping

    while text_list[-1][-1] not in end_characters:
        first_word = text_list[-2]
        second_word = text_list[-1]
            # look up the start bigram in the dictionary
            # add a random item from its associated values to the end 
        text_list.append(random.choice(chains[first_word, second_word]))
    text_string = ' '.join(text_list)
    # if the string is less than or equal to 140 characters
    if len(text_string) <= 140:
        return text_string
    else:
        return make_text(chains)


# function to tweet the sentence
def tweet_sentence(some_text):
    key = os.environ.get("TWITTER_API_KEY")
    key_secret = os.environ.get("TWITTER_API_SECRET")
    access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

    api = twitter.Api(consumer_key = key,
                      consumer_secret = key_secret,
                      access_token_key = access_token,
                      access_token_secret = access_token_secret)   

    api.PostUpdate(some_text)
  
def main():
    args = sys.argv

    #Change this to read input_text from a file
    input_text = filename

    chain_dict = make_chains(input_text, ngram)
    random_text = make_text(chain_dict)
    # tweet_sentence(random_text)
    print random_text

if __name__ == "__main__":
    main()