#ori berman
import sys
def count_sequences(raw_sequence):
    listseq = raw_sequence.replace("X", "")
    listseq = listseq.split() #split subsequences into a list
    print(f"\nthe number of sequences submited is {len(listseq)}") #answer to question 1- how many sequenced were submitted in total
    return listseq