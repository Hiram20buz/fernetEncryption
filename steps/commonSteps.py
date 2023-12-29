import os
import sys
from cryptography.fernet import Fernet


def generateKey(file_path: str = "thekey.key"):
    key = Fernet.generate_key()
    with open(file_path, "wb") as thekey:
        thekey.write(key)


def readKey(file_path: str = "thekey.key") -> str:
    with open(file_path, "rb") as key:
        return key.read()


def encrypt_file(file: str, key: str, encrypt: bool = True):
    with open(file, "rb") as thefile:
        contents = thefile.read()
    if encrypt:
        contents_file = Fernet(key).encrypt(contents)
    else:
        contents_file = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_file)


def encrypt_dir(directory_to_encrypt: str, key: str, encrypt: bool = True):
    for root, dirs, files in os.walk(directory_to_encrypt):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            encrypt_file(file_path, key, encrypt)

            
