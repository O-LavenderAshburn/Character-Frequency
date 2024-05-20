"""
Script to count the frequency of characters that apair in cyphertext

"""


def analyse_cyphertext():
    """Read in Cyphertext and write out frequency"""
    dictionarys = []
    freq == [0] * 99
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


global freq
global dictionarys

analyse_cyphertext()
