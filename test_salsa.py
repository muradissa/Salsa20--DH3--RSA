#!/usr/bin/env python
from salsa import Salsa
import codecs

def print_state(s):
  assert len(s) == 16
  for i in range(4):
    # print "{:08x} {:08x} {:08x} {:08x}".format(s[4*i],s[4*i+1],s[4*i+2],s[4*i+3])
    print(f"{s[4*i]}, {s[4*i+1]},{s[4*i+2]}, {s[4*i+3]}")


def test_salsa():
    salsa20 = Salsa()

    vectors = [ 
        [ range(1,33), [3,1,4,1,5,9,2,6], [7,0,0,0,0,0,0,0], 
        [ 0xb9a205a3,0x0695e150,0xaa94881a,0xadb7b12c,
        0x798942d4,0x26107016,0x64edb1a4,0x2d27173f,
        0xb1c7f1fa,0x62066edc,0xe035fa23,0xc4496f04,
        0x2131e6b3,0x810bde28,0xf62cb407,0x6bdede3d ] ] ]

    for i in range(len(vectors)):
        v = vectors[i]
        s =  salsa20(v[0],v[1],v[2]) 
        w = s[:] # faltten the matrix
        print_state(s)
        print(w)
        assert s == v[3]
    print( "All tests passed!") 

def test_rot132():
    salsa20 = Salsa()
    w = 0xbfffffff
    r=4
    print(hex(w))
    w = salsa20._rotl32(w, r)
    print(hex(w))

def test_littleendian():
    salsa20 = Salsa()
    w = [0x21,0x43,0x65,0x87]
    r = salsa20._littleendian(w)
    print(hex(r))
    w = range(1,5)
    r = salsa20._littleendian(w)
    print(hex(r))

def test_num_key_to_list():
    salsa20 = Salsa()
    key = 0x12345678
    w = salsa20.num_key_to_list(key)
    print(w)
    r = salsa20._littleendian(w)
    print(hex(r))

def test_enc():
    msg = ["abcd","higk","lmno","pqrs"]*4
    x = "".join("{:02x}".format(ord(c)) for c in msg[0])
    print(x)
    msg = [ "".join("{:02x}".format(ord(c)) for c in text) for text in msg]
    imsg = [ int(text,16) for text in msg]
    print(hex(imsg[0]))
    param = [ range(1,33), [3,1,4,1,5,9,2,6], [7,0,0,0,0,0,0,0]]
    salsa20 = Salsa()
    s = salsa20(param[0],param[1],param[2])
    print(imsg)
    ct = salsa20.encrypt(imsg)
    print(ct)
    pt = salsa20.encrypt(ct)
    print(pt)
    y = bytes.fromhex(hex(pt[0])[2:]).decode('ascii')
    print(y)

# test_rot132()
# test_salsa()
# test_littleendian()
# test_num_key_to_list()
test_enc()