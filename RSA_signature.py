import random
from hashlib import sha256
import p_and_g
from p_and_g import PrimesAndCreators


def hash_msg(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed

# for generate_rsa_keys function
def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# for generate_rsa_keys function
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m


def generate_rsa_keys():
    PAC = p_and_g.PrimesAndCreators()
    p = PAC.get_random_p()
    q = PAC.get_random_p() # no check if p == q needed because this is different arrays,
    #Should check above line need to check if p==q
    #
    #
    #
    #
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = coprime(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = modinv(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def create_signiture(privatek, hashedMessage):
    # Unpack the key into it's components
    key, n = privatek

    # Convert each letter in the hashed text to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in hashedMessage]

    # Return the array of bytes
    return cipher


def decrypte_signiture(publick, ciphertext):
    # Unpack the key into its components
    key, n = publick

    # Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow(char, key, n) for char in ciphertext]
    try:
        plain = [chr(pow(char, key, n)) for char in ciphertext]
    # In case that the key cipher a non ascii numbers (wrong key)
    except:
        return None

    # print("Decrypted number representation is: ", numberRepr)

    # Return the array of bytes as a string
    return ''.join(plain)


def hash_func(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed


def verify(HashedMessage, decriptedSignature):
   # ourHashed = hashFunction(message)
    if HashedMessage == decriptedSignature:
        # print("Verification successful: ", )
        # print(HashedMessage, " = ", decriptedSignature)
        return True
    else:

        # print("Verification failed")
        # print(HashedMessage, " != ", decriptedSignature)
        return False

