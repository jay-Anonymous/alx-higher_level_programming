#!/usr/bin/python3

"""
Docstring goes here

"""


def multiple_returns(sentence):
    sen_len = len(sentence)
    prem_char = sentence[0]
    if sen_len == 0:
        return (sen_len, None)
    else:
        return (sen_len, prem_char)

if __name__ == '__main__':
    sentence = 'Cheesy chunky chimey chutney'
    multiple_returns(sentence)
