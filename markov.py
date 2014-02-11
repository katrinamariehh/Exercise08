#!/usr/bin/env python

from sys import argv

script, filename = argv

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
    print word_list
    # use a for loop to create tuples to be the keys in the dictionary
    d = {}
    for i in range(len(word_list)-2):
        d[word_list[i], word_list[i + 1]] = word_list[i + 2]
    #return d
    print d
make_chains(filename)
'''def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
  #  main()
'''