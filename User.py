from globals import *
from RSA_signature import create_signiture, generate_rsa_keys, decrypte_signiture , hash_func
from Salsa_UI import encrypte, decrypte
from datetime import datetime

class User:
    	
    def __init__(self, name, id):

        self.dh_private_key = dh.generate_private_key(BITS)
        self.name = name
        self.id = id
        self.dh_mutual_key = 1
        self.index = f"{name}-{id}"
        self._rsa_private_key , public_rsa_keys[self.index] = generate_rsa_keys()
         

    def send_key_msg(self):

        # Prevent from the first sender to validate the signiture  
        Digets = hash_func(str(key_msg['X']) + str(key_msg['X^y']))          
        if key_msg['signiture'] != "" and  Digets != decrypte_signiture(public_rsa_keys[key_msg['sender']], key_msg['signiture']):
            print("**Danger!! Unrecognized sender!!!")
            exit(0)


        if (key_msg['X^y'] != ""):
            self.dh_mutual_key = dh.get_mutual_K(key_msg['X^y'], self.dh_private_key)

        if (key_msg['X'] != ""):
            key_msg['X^y'] = dh.get_mutual_K(key_msg['X'], self.dh_private_key)

        key_msg['X'] = dh.get_my_public(self.dh_private_key)#g^e1
        
        key_msg['signiture'] = create_signiture( self._rsa_private_key, hash_func(str(key_msg['X']) + str(key_msg['X^y'])))

        key_msg['sender'] = self.index


    def send_msg(self, msg):
        
        str_msg['msg'] = encrypte(msg, self.dh_mutual_key )
        str_msg['signiture'] = create_signiture(self._rsa_private_key , hash_func(msg))
        str_msg['sender'] = self.index
    

    def get_msg(self):

        orig_msg = decrypte(str_msg['msg'],  self.dh_mutual_key)
        
        Digets = hash_func(orig_msg) 
                            
        if Digets == decrypte_signiture( public_rsa_keys[str_msg['sender']], str_msg['signiture']):
            return {
            'from' : str_msg['sender'], 
            'at' : datetime.now().strftime("%H:%M:%S"), 
            'msg' : orig_msg
            }

        return {'from' : 'Unknown' , 'msg' : ''}
                    