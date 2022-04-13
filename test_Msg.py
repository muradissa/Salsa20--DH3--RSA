from Msg import Msg

msg = "abcdef"
i = Msg(msg)

def test_Msg():
    # msg_list is for internall use for enc
    print(i.msg_list)
    print(i.to_string())

def tes_hex():
    hexa = i.to_hex()
    print(hexa)
    print(Msg.hex_list_to_string(hexa))

test_Msg()
tes_hex()