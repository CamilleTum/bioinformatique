#!/usr/bin/env python

from Bio import SeqIO

def my_read(filename):
    ftype =''
    if filename.endswith('.fna'):
        ftype = "fasta"
    elif filename.endswith('.gb'):
        ftype = "genbank"
    else:
        print "Unknown file type"
        return None
    record = SeqIO.read(filename,ftype)
    return record

