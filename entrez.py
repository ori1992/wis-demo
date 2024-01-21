#opn3
from Bio import Entrez
Entrez.email = "ori.berman@weizmann.ac.il"

SEARCH_TERM = input('please enter a term you would like to search \n')
N = input('How many enteries would you like to download?')

handle = Entrez.esearch(db="nucleotide", term=SEARCH_TERM, idtype="acc", retmax=N)
record = Entrez.read(handle)



