import os
from Bio import SeqIO

def get_records(filename="lab4/output/sequences.gb"):
    if not os.path.exists(filename):
        filename = "output/sequences.gb"
    return list(SeqIO.parse(filename, "genbank"))
