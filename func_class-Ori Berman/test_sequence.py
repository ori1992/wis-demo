# ori berman
from sequence import (
    sequence_prep,
    count_charcter_in_x,
    precent,
)  # importing functions writen in sequence.py file

filename = "sequence.txt "  # entering a file name with a space to check for errors


def test_sequence_prep():  # testing thr function sequence_prep
    (raw_seq, list_seq) = sequence_prep(filename)
    assert raw_seq == "AACCXGGTXT"  # this can be changed depending on the file provided
    assert list_seq == [
        "AA",
        "CC",
        "GG",
        "TT",
    ]  # this can be changed depending on the file provided


def test_counter():  # testing thr function sequence_prep
    (raw_seq, list_seq) = sequence_prep(filename)
    raw_seq = count_charcter_in_x(raw_seq)
    list_seq = count_charcter_in_x(list_seq)
    assert raw_seq == {
        "A": 2,
        "C": 2,
        "G": 2,
        "T": 2,
        "X": 2,
    }  # this can be changed depending on the file provided
    assert list_seq == {
        "AA": 1,
        "CC": 1,
        "GG": 1,
        "TT": 1,
    }  # this can be changed depending on the file provided


def test_precent():  # testing thr function sequence_prep
    (raw_seq, list_seq) = sequence_prep(filename)
    basecounter = count_charcter_in_x(raw_seq)
    basecounter = precent(basecounter)
    assert basecounter == {
        "A": 20.0,
        "C": 20.0,
        "G": 20.0,
        "T": 20.0,
        "X": 20.0,
    }  # this can be changed depending on the file provided
