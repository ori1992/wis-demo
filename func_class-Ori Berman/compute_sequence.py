# Ori Berman

from sequence import (
    sequence_prep,
    count_charcter_in_x,
    precent,
)  # importing functions writen in sequence.py file
import sys

if (
    len(sys.argv) != 2
):  # making sure the program was ran with the correct ampunt of variables
    exit(f"Usage: {sys.argv[0]} File Name")

filename = sys.argv[1]

(raw_seq, list_seq) = sequence_prep(filename)
print(
    f"\nthe number of sequences submited is {len(list_seq)}"
)  # answer to question 1- how many sequenced were submitted in total

seqcounter = count_charcter_in_x(list_seq)
print(
    f"\nThose are the subsequences and how many times they appear:\n{seqcounter}"
)  # answer to question 2- how many subsequences are there and how many times they appear

basecounter = count_charcter_in_x(raw_seq)
basecounter["Error"] = basecounter[
    "X"
]  # change the name of X to Errors for clarification
del basecounter["X"]  # delet old X to avoid repetions

print(
    f"\nThose are the bases and how many times they appear:\n{basecounter}"
)  # answer to question 3- how many times each base appers in the sequences provided

basefreq = precent(basecounter)
print(
    f"\nThe frequency of each base from all total bases submited:\n{basefreq}"
)  # answer to question 4- what is the frequency of each base and the errors.
