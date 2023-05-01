#!/usr/bin/env python3

def return_evens(num_list):
    number = [num for num in num_list if num % 2 == 0]
    return number

def make_exclamation(sentence_list):
    exclamation = [word + "!" for word in sentence_list]
    return exclamation