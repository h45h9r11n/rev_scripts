import idaapi
import idc
import struct

bin = ""
file = open("dumped.bin", "wb")
for ea in range (0x960000, 0x960000, 4):
    bin += struct.pack("<L", idc.Dword(ea))

file.write(bin)
file.close()