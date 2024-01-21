# ori berman
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import sys


def protein_data_for_conversion(File):
    File = File.rstrip(" ")  # strip file name from any spaces
    with open(File) as f:  # open file
        prot = f.read()
    prot_sum = {}
    proteins = SeqIO.parse(File, "fasta")  # convert fasta file to SeqIO
    i = 0
    for record in proteins:  # for loop to go through all the proteins downloded
        prot_an = ProteinAnalysis(record.seq)  # analyse each protein
        prot_sum[i] = (
            record.description,
            prot_an.molar_extinction_coefficient(),
            round(prot_an.molecular_weight()),
        )  # save extinction coefficient
        # weight = round(prot_an.molecular_weight()) #save molecular weight
        print(
            f"the protein {prot_sum[i][0]} weight is {prot_sum[i][2]} and extinction coefficient is: {prot_sum[i][1][0]} when reduced and {prot_sum[i][1][1]} when oxidized"
        )
        i = i + 1
    return prot_sum
    # this two variables were chosen because they are important to convert the absorbance in 280 nm of a solution into the concentration of a purified protein


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()
File = sys.argv[1]
prot_sum = protein_data_for_conversion(File)


f = open("protein_MW_and_cof.txt", "w")  # open file for writing
f.write(str(prot_sum))  # write file
f.close()  # close file
