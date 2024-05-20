import os
import math
from operator import itemgetter


freq = [0] * 99
dictionarys = []


def analyse_cyphertext():
    # open file
    with open("ciphertext2.txt", "r") as file:
        content = file.read()
        words = content.split()

    # find tally of nubers
    for i in range(len(words)):
        value = int(words[i])
        freq[value] += 1

    # open file
    with open("freq.txt", "w") as file:
        total = 0
        for i in range(len(freq)):
            if freq[i] != 0:
                total += 1
                file.write("%2d,%2d \n" % (i, freq[i]))

                # create dictinary for unique number and value
                cypehr = {"num": i, "frequency": freq[i]}
                dictionarys.append(cypehr)
                file.newlines

        # write total
        file.write("total: %2d" % (total))


def decrypt(mapped_dict):
    # read and close cypher_text2
    cypher_text = open("ciphertext2.txt", "r")
    text = cypher_text.read()
    numbers = text.split(" ")
    cypher_text.close()

    with open("decypher.txt", "w") as file:

        for i in range(len(numbers)):
            current_num = numbers[i]
            letter = get_mapped(mapped_dict, current_num)
            if letter is not None:
                file.write(letter)


analyse_cyphertext()
