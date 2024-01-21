#ori berman
from sequence import sequence_prep, count_charcter_in_x

filename = "sequence.txt "
def test_sequence_prep():
    (raw_seq, list_seq) = sequence_prep(filename)
    assert(raw_seq == "AACCXGGTXT")
    assert(list_seq == ["AA", "CC", "GG", "TT"])



(list_seq, raw_seq) = sequence_prep(filename)
def test_how_many_sequences():
    seq_num = sequence_prep(raw_seq)
    assert(len(seq_num) == 4)



def test_counter():
    num = count_charcter_in_x(list_seq)
    assert(num == {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'X':2})

