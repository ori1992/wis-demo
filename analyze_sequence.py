#Ori Berman
filename = input("please enter the file name, make sure the name does not contain any spaces:") #ask user to provide the file name
filename = filename.rstrip(" ") #strip file name from any spaces
with open(filename) as f:
    rawsequence = f.read() #open the file with the file name provided

rawsequence = rawsequence.replace("\n", "").upper() #delete new raws
listseq = rawsequence.replace("X", "") #prepare new variable of susequences without the errors
rawsequence = rawsequence.replace(" ", "") #delete spaces from the raw sequence
listseq = listseq.split() #split subsequences into a list
print(f"\nthe number of sequences submited is {len(listseq)}") #answer to question 1- how many sequenced were submitted in total

seqcounter = {}  # dictionary to count subsequences
for character in listseq:  # for loop to count subsequences
    if character not in seqcounter:
        seqcounter[character] = 1
    else:
        seqcounter[character] += 1
print(f"\nThose are the subsequences and how many times they appear:\n{seqcounter}") #answer to question 2- how many subsequences are there and how many times they appear

basecounter = {}  # dictionary to count how many of each base in the raw sequene
for character in rawsequence:  # for loop to count how many of each base in the raw sequene
    if character not in basecounter:
        basecounter[character] = 1
    else:
        basecounter[character] += 1
basecounter["Error"] = basecounter["X"] #change the name of X to Errors for clarification
del basecounter["X"] #delet olf X to avoid repetions

print(f"\nThose are the bases and how many times they appear:\n{basecounter}") #answer to question 3- how many times each base appers in the sequences provided

sumchar = sum(basecounter.values()) #how many bases are ther in total (100%)
basefreq = {} # dictionary to sum bases frequencies 
for character in basecounter:  # for loop to sum bases frequencies 
    basefreq[character] = round(basecounter[character] / sumchar * 100,1)
print(f"\nThe frequency of each base from all total bases submited:\n{basefreq}") #answer to question 4- what is the frequency of each base and the errors.
