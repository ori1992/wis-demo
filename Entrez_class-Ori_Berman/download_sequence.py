# ori berman
import sys


def download_prot_seq(SEARCH_TERM, N):
    from Bio import Entrez

    Entrez.email = "ori.berman@weizmann.ac.il"

    handle = Entrez.esearch(
        db="protein", term=SEARCH_TERM, sort="relevance", idtype="acc", retmax=N
    )  # search for the protein data of a type of protein asked for, no more than N enteries
    record = Entrez.read(handle)
    handle.close()

    file = Entrez.efetch(
        db="protein", id=record["IdList"], rettype="fasta", retmode="text"
    )  # fetch the data of the proteins that came out of the search
    data = file.read()
    file.close()
    return data


if len(sys.argv) != 3:
    print(
        f"Usage: {sys.argv[0]} FILENAME ; name of protein; number: how many enteries you would like to download)"
    )
    exit()


SEARCH_TERM = sys.argv[1]
N = int(sys.argv[2])
data = download_prot_seq(SEARCH_TERM, N)
with open(
    "prot.fasta", "w"
) as fh:  # save the data of the proteins in a file called 'prot.fasta'
    fh.write(data)
