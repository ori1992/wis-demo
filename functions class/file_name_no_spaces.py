#ori berman
import sys
def name_no_space(file_name):
    file_name = file_name.rstrip(" ") #strip file name from any spaces
    with open(file_name) as f:
        raw_sequence = f.read() #open the file with the file name provided
    raw_sequence = raw_sequence.replace("\n", "").upper() #delete new raws
    return raw_sequence