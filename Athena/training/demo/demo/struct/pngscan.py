"""Print the chunk types and lengths of the data in a PNG file.

This script demonstrates the use of the 'struct' module to parse binary data.

Many binary file formats also include CRC fields for internal error checking.
This script uses binascii.crc32 to compute the CRC of the data in each PNG
chunk.
"""

import sys
import struct
import binascii

if len(sys.argv) != 2:
    print "use: pngscan.py some_file.png"
    sys.exit(0)

filename = sys.argv[1]
pngfile = open(filename, 'rb')

# Get and print the 8 byte PNG signature.
sig = pngfile.read(8)
print "8 byte PNG signature:",
for c in sig:
    print "{:02X}".format(ord(c)),
print " ", repr(sig)

print "\nChunks:"
print "{:4s} {:>10s}  {:s}".format("Type", "Length", "CRC")

# Read the chunks, and print the chunk type and length.
while True:
    s8 = pngfile.read(8)
    if len(s8) == 0:
        break
    # Use struct.unpack to parse the first 8 bytes into the length and type.
    chunk_len, chunk_type = struct.unpack(">I4s", s8)

    chunk_data = pngfile.read(chunk_len)

    s4 = pngfile.read(4)
    # Use struct.unpack to parse the CRC value as a signed integer.
    chunk_crc, = struct.unpack(">i", s4)

    crc32 = binascii.crc32(chunk_type + chunk_data)
    if crc32 == chunk_crc:
        chunk_status = "OK"
    else:
        chunk_status = "ERROR"

    print "{:4s} {:10d}  {}".format(chunk_type, chunk_len, chunk_status)

pngfile.close()
