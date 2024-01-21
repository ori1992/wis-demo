#ori berman
import sys
def count_charcter_in_listseq(listseq):
    counter = {}  # dictionary to count subsequences
    for character in listseq:  # for loop to count subsequences
        if character not in counter:
            counter[character] = 1
        else:
            counter[character] += 1
    return counter
    

