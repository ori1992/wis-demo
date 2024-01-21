# ori berman
from analyze import protein_data_for_conversion


def test_protein_data_for_conversion():
    file = "prot.fasta"
    prot_data = protein_data_for_conversion(file)
    assert (
        prot_data[0][2] == 69323
    )  # this can be changed values taken from the literture for each protein
    assert (
        prot_data[0][1][0] == 47790
    )  # this can be changed values taken from the literture for each protein
    assert (
        prot_data[0][1][1] == 49915
    )  # this can be changed values taken from the literture for each protein
