#!/usr/bin/env python

import sys

from seq_record import *
from seq import *

if __name__=="__main__":
    for fname in sys.argv[1:]:
        record = my_read(fname)
        print fname
        print get_GC_contents(record.seq)
        print get_len(record.seq)
        print record.features

