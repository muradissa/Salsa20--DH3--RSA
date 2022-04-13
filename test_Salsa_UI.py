from Salsa_UI import Salsa_UI, encrypte, decrypte
from Msg import Msg

def test_enc():
    key = range(1,33)
    s = Salsa_UI(key)
    msg ="abcdefghijklmnopqrs"*4
    emsg_hex = s.encrypte(msg)
    print(emsg_hex)
    ptxt_hex_list = s.decrepte(emsg_hex)
    ptxt = Msg.hex_list_to_string(ptxt_hex_list)
    print(ptxt)

def test_enc_dec_interface():
    key = 1234
    msg = "hi"
    c_msg = encrypte(msg, key)
    dc_msg = decrypte(c_msg,key)
    print(dc_msg)


test_enc_dec_interface()