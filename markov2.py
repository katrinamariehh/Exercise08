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
        word_list[i] = word_list[i].strip('_--+=[]{}<>()')

    chains = {}
    # TODO a default of 2 of no length is given?
    # iterating over the word list
    for i in range(len(word_list) - int(ngram_length)):
        # iterating over the length of the ngram
        ngram = []
        for j in range(int(ngram_length) + 1):
            # each word in the ngram can be referenced as the i index plus the j index
            ngram.append(word_list[i+j])
        # but this makes ngram a list and to be a key in the dictionary it needs to be a tuple
        ngram_key = tuple(ngram[:-1])
        ngram_value = ngram[-1]
        # this looks up the ngram in the dictionary
        if chains.get(ngram_key):
            # adds the value if the ngram is already present
            chains[ngram_key].append(ngram_value)
        else:
            # and creates the initial key-value pair if the ngram is not present
            chains[ngram_key] = [ngram_value]

    return chains

chains = make_chains(filename, ngram)


def make_tuple(dictionary):
    # select a random key value from the dictionary
    while True:
        start_ngram = random.choice(chains.keys())
        if start_ngram[0].istitle():
            return start_ngram


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # start with a random tuple from the dictionary
    start_ngram = make_tuple(chains)
    ngram_length = len(start_ngram)
    text_list = []
    # adding the starting ngram to the text_list to be made into a text_string
    for item in start_ngram:
        text_list.append(item)
    # establishing characters to end the sentence with
    end_characters = ['.', '?', '!', '"', '!"', '?"', '."']
    # while the last character of the last item is not in end_characters, keeping looping
    while text_list[-1][-1] not in end_characters:
        current_ngram = (tuple(text_list[-ngram_length:]))
        available_words = chains[current_ngram]
        next_word = random.choice(available_words)
        text_list.append(next_word)
        # text_list.append(random.choice(chains[(text_list[-ngram_length:])]))
    text_string = " ".join(text_list)
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