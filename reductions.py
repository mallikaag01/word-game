# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Mallika Gupta
Date: February 17, 2023
"""
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []

        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

## The function reduceOne takes two strings and the wordlist to determine
## if the second string can be reduced from the first string. It returns a boolean
## value. #

def reduceOne(firstString, secondString, wordlist):
    if secondString not in wordlist:
        return False
    if firstString not in wordlist:
        return False

    wordset = set(wordlist)
    for i in range(len(firstString)):
        for j in range(i + 1, len(firstString) + 1):
            substring = firstString[i:j]
            if substring in wordset and firstString[:i] + firstString[j:] == secondString:
                return True
    return False

## The function reduceAll determines all word reductions that can be obtained
## from the input word after removing one letter. It returns a list of words.s

def reduceAll(word, wordlist):
    reduced_words = []
    for i in range(len(word)):
        reduced_word = word[:i] + word[i+1:]
        if reduced_word in wordlist:
            reduced_words.append(reduced_word)
    return reduced_words

## The function reduceTwoAll takes two arguments which are word and wordlist.
## The for loop iterates first through all possible positions of the first letter 
## to remove and does the same for the second letter as well. It removes the 
## two letters and if the twice-reduced word is present in the wordlist,it 
## adds it to the list of twice-reduced words.
def reduceTwoAll(word, wordlist):
    twice_reduced_words = []
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            twice_reduced_word = word[:i] + word[i+1:j] + word[j+1:]
            if twice_reduced_word in wordlist:
                twice_reduced_words.append(twice_reduced_word)
    return twice_reduced_words


## This function validateReduction tests both the conditions which reduces the 
## length of the word and checks if the word is valid. If the word is valid, 
## the function returns True. Otherwise, it returns False.

def validateReduction(reductions, wordlist):
    for i in range(len(reductions) - 1):
        if not reduceOne(reductions[i], reductions[i+1],  wordlist):
            return False
    return True

## This function calls the four test cases provided written below and also 
## loads the words given in the wordlist.
def main():
    wordlist = loadWords()
    testReduceOne(wordlist)
    testReduceAll(wordlist)
    testReduceTwoAll(wordlist)
    testValidateReduction(wordlist)

###############################################################

## Here is where you will write your test case functions

## The below test which is called testReduceOne checks whether the first string
## can reduce to the second string. It returns a boolean value True or False if
## the reduction is valid.
def testReduceOne(wordlist):
    assert reduceOne("leave", "eave", wordlist) == True
    assert reduceOne("beleve", "eleve", wordlist) == True
    assert reduceOne("believe", "elieve", wordlist) == False
    assert reduceOne("agave", "gave", wordlist) == True
    assert reduceOne("artt","art",wordlist)==False

# The below test which is called testReduceAll takes a collection of strings
# which can be reduced from the provided string word. The function takes a
# string and a list as parameters to return a list of possible reduced words.

def testReduceAll(wordlist):
    assert reduceAll("boats", wordlist) == [
        "oats", "bats", "bots", "boas", "boat"]
    assert reduceAll("moats", wordlist) == [
        "oats", "mats", "mots", "moas", "moat"]
    assert reduceAll("boats", wordlist) == [
        "oats", "bats", "bots", "boas", "boat"]
    assert reduceAll("moats", wordlist) == [
        "oats", "mats", "mots", "moas", "moat"]

## The below test which is called testReduceTwoAll helps to create a collection
## of strings which are reduced from a provided string word by removing two
## characters. This function specifically takes a string and list as parameters.
## It returns a list of possible twice-reduced words.
def testReduceTwoAll(wordlist):
    assert reduceTwoAll("geary", wordlist) == [
        "ary", "ear", "gry", "gay", "gar", "gey", "ger"]
    assert reduceTwoAll("weary", wordlist) == [
        "ary", "ear", "wry", "way", "war", "wey", "wer", "wea"]
    assert reduceTwoAll("teary", wordlist) == [
        "ary", "ear", "try", "tay", "tar", "ter", "tea"]
    assert reduceTwoAll("leary", wordlist) == [
        "ary", "ear", "lay", "lar", "ley", "ler", "lea"]

## The below test testValidationReduction checks whether both the character
## removal and validity are there. For example, the word proven can not be reduced
## to prven, so it return False.
def testValidateReduction(wordlist):
    assert validateReduction(["proven", "prven"], wordlist) == False
    assert validateReduction(
        ["turnables", "turnable", "tunable", "unable"], wordlist) == False
    assert validateReduction(["boas", "oats,oat,at"], wordlist) == False
    assert validateReduction(["proven", "prven"], wordlist) == False
    assert validateReduction(["artt", "art"], wordlist) == False

###############################################################
if __name__ == "__main__":
    main()
