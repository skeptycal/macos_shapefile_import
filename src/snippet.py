from struct import pack, unpack, calcsize, error, Struct
import os
import sys
import time
import array
import tempfile
import warnings
import io
from datetime import date

if PYTHON3:
    xrange = range
    izip = zip
else:
    from itertools import izip
