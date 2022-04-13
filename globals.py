from DH_algo import DH_algo as DH

BITS = 16    # instead of 32

dh = DH()

public_rsa_keys = {}

key_msg = {
    'X' : "",#g^ Ei
    'X^y' : "",#g ^ Ei*Ej
    'signiture' : "",
    'sender' : ""
}

str_msg = {
    'msg' : [],
    'signiture':"",
    'sender' : ""
     }



# The input here have to be User objects
def generate_mutual_K_for_3(user_1,user_2,user_3):

    user_1.send_key_msg()
    user_2.send_key_msg()
    user_3.send_key_msg()
    user_1.send_key_msg()
    user_2.send_key_msg()

# In case that the mutual key generated to be equal to 1, every user generate anouther
# private key to avoid this situation
    while user_1.dh_mutual_key == 1:
        user_1.dh_private_key = dh.generate_private_key(BITS)
        user_2.dh_private_key = dh.generate_private_key(BITS)
        user_3.dh_private_key = dh.generate_private_key(BITS)
        user_1.send_key_msg()
        user_2.send_key_msg()
        user_3.send_key_msg()
        user_1.send_key_msg()
        user_2.send_key_msg()



        