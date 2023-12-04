#!/usr/bin/python3
def multiple_returns(sentence):
    senlen = len(sentence)
    if senlen > 0:
        return senlen, sentence[0]
    return(0, None)
