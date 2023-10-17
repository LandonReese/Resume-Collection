# Chat Encryption Helper - ch9_crypto_chat.py
import os, base64, json
#from Crypto.Cipher import PKCS1_OAEP, AES
#from Crypto.PublicKey import RSA, ECC
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
 
# encryption method used by all calls
def encrypt(message, usePKI, useDH, dhSecret):
    em=cipherEncrypt(message, dhSecret, 1)
    return em
 
# decryption method used by all calls
def decrypt(message, usePKI, useDH, dhSecret):
    dm=cipherEncrypt(message, dhSecret, -1)
    return dm
 
# decrypt using RSA (for future reference, not needed for this homework)
#def decrypt_rsa(ciphertext):
#    return ciphertext
 
# encrypt using RSA (for future reference, not needed for this homework)
#def encrypt_rsa(message):
#    return message
 
# check client commands (for future reference, not needed for this homework)
def check_client_command(data):
    return 1
 
# check server commands (for future reference, not needed for this homework)
def check_server_command(data):
    return 1
    
def reversed_string(a_string):
    return a_string[::-1]

def cipherEncrypt(inputText, n, d):
    reverseText = ""
    encryptedText = ""
    N = 0       # number of positions to shift characters in the inputText by. N>=1
    D = 0       # direction of shift, D can be either be 1 (right) or -1 (left)

    # 1. Reverse the input text
    reverseText = "".join(reversed(inputText))

    # 2. Shift all the ASCII characters in reversed input text by “N” positions.
    for char in reverseText:
        x = ord(char)           # x is the ASCII value of our character
        y = n * d               # N * D = Our shift amount in the positive or negative direction
        x += y                  # x is now an incremented ascii value
        #lets say x = 45, shifted left 20. x now is 25
        while x < 34:
            x+=126
        while x > 126:
            x-=126
        
        character = chr(x)
        encryptedText = encryptedText + character
        # print("Text:    " + text)
        # print("Encrypt: " + encryptedText)
    return encryptedText
#Enter your code here for custom encryption from Lab 3
    # return result
