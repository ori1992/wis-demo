from Bio.Seq import Seq 
from Bio import SeqIO
import requests
from Bio import Entrez
Entrez.tool = 'Demoscript'
Entrez.email = "ori.berman@weizmann.ac.il"
info = Entrez.einfo()
data = info.read() 
print(data) 