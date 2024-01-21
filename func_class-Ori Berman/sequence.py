# ori berman
import sys


def sequence_prep(filename):  # function that uploads a text file and
    file_name = filename.rstrip(" ")  # strip file name from any spaces
    with open(filename) as f:
        raw_sequence = f.read()  # open the file with the file name provided
    raw_sequence = raw_sequence.replace("\n", "").upper()  # delete new raws
    listseq = raw_sequence.replace("X", "")  # delete errors
    listseq = listseq.split()  # split subsequences into a list
    raw_sequence = raw_sequence.replace(" ", "")  # delete spaces from the raw sequence
    return raw_sequence, listseq


def count_charcter_in_x(x):
    counter = {}  # dictionary to count charcters in x
    for character in x:  # for loop to count charcters in x
        if character not in counter:
            counter[character] = 1
        else:
            counter[character] += 1
    return counter


def precent(basecounter):
    sumchar = sum(basecounter.values())  # how many bases are ther in total (100%)
    basefreq = {}  # dictionary to sum bases frequencies
    for character in basecounter:  # for loop to sum bases frequencies
        basefreq[character] = round(basecounter[character] / sumchar * 100, 1)
    return basefreq
