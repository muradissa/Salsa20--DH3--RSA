from salsa import Salsa 
from Msg import Msg

def encrypte(msg, dh_mutual_key):
    salsa = Salsa_UI(dh_mutual_key)
    c_msg = salsa.encrypte(msg)
    return c_msg

def decrypte(c_msg, dh_mutual_key):
    salsa = Salsa_UI(dh_mutual_key)
    msg = salsa.decrepte(c_msg)
    return msg.rstrip()
class Salsa_UI:
    def __init__(self, key):
        assert key != 0
        self._nonce = [3,1,4,1,5,9,2,6]
        self._s20 = Salsa()
        self._key = []
        key = abs(key)
        while key != 0:
            self._key.append(key % 256) # 1 byte
            key //= 256
        
        assert len( self._key ) < 33 

        while len( self._key) < 32:
            self._key.append(0)

        

    def encrypte(self, string):
        msg = Msg(string) 
        hmsg = msg.to_hex()
        return self._calc_encrypte_by_hex_list(hmsg)

    
    def _calc_encrypte_by_hex_list(self, hmsg):
        word_size = 2^32 
        num_word = 16

        cypher_hash_text_list = []
        for i in range(0,len(hmsg)//num_word ):# i - 0 --> block_counter = [0,0,0,0,0,0,0,0,0]
            block_counter = [int(x) for x in hex(i)[2:]] 
            if len(block_counter) < 8:
                block_counter.extend((8-len(block_counter))*[0]) 
            self._s20(self._key,self._nonce,block_counter[0:8]) # clac internal enc matrix
            ctext_list = self._s20.encrypt(hmsg[i*num_word:( i + 1 )*num_word]) # use the calc matrix to enc
            cypher_hash_text_list.extend(ctext_list)
        
        return cypher_hash_text_list
    def decrepte(self, chextxt):
        """ chextxt is list of hex value similar to result of Msg.to_hex() """
        list_num =  self._calc_encrypte_by_hex_list(chextxt)
        return Msg.hex_list_to_string(list_num)