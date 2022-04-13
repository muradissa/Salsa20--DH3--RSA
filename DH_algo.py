from p_and_g import PrimesAndCreators
from random import getrandbits

class DH_algo:
    primeNums = PrimesAndCreators()
    
    def __init__(self):
        self.generate_p_and_g()

    def generate_p_and_g(self):
        p = self.primeNums.get_random_p()
        # loop until finding creator g:
        while True:
            tmp = p - 1
            g = self.primeNums.get_random_g()
            if g < 1 or g > p - 2:
                continue
            lis = []
            divider = 2
            # find the prime numbers that compose (p - 1)
            while tmp > 1:
            	while tmp % divider == 0:
            			if divider not in lis:
            					lis.append(divider)
            			tmp /= divider
            	divider +=1
            # print(f"lis is {lis}")
            # check that gcd(g^x , p - 1) == 1 for each x belongs to lis
            cnt = 0
            for x in lis:
            		if pow(g, x, p) != 1:
            				cnt+=1

            if cnt == len(lis):
                self.p = p
                self.g = g
                return

    def get_my_public(self, pr_key):
        return (self.g ** pr_key) % self.p

    def get_mutual_K(self, X, pr_key):
        return (X ** pr_key) % self.p

    def generate_private_key(self, bits):

        key = getrandbits(bits)
        while key > (self.p - 2) or key < 1:
            key = getrandbits(bits)
        
        return key