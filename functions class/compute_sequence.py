#Ori Berman
from sequence import sequence_prep, count_charcter_in_x
filename = "sequence.txt "

(list_seq, raw_seq) = sequence_prep(filename)
print(f"\nthe number of sequences submited is {len(list_seq)}") #answer to question 1- how many sequenced were submitted in total

seqcounter = count_charcter_in_x (list_seq)
print(f"\nThose are the subsequences and how many times they appear:\n{seqcounter}") #answer to question 2- how many subsequences are there and how many times they appear

basecounterounter = count_charcter_in_x (raw_seq)
basecounter = {}  # dictionary to count how many of each base in the raw sequene
basecounter["Error"] = basecounter["X"] #change the name of X to Errors for clarification
del basecounter["X"] #delet olf X to avoid repetions

print(f"\nThose are the bases and how many times they appear:\n{basecounter}") #answer to question 3- how many times each base appers in the sequences provided

sumchar = sum(basecounter.values()) #how many bases are ther in total (100%)
basefreq = {} # dictionary to sum bases frequencies 
for character in basecounter:  # for loop to sum bases frequencies 
    basefreq[character] = round(basecounter[character] / sumchar * 100,1)
print(f"\nThe frequency of each base from all total bases submited:\n{basefreq}") #answer to question 4- what is the frequency of each base and the errors.

