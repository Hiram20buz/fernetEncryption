import commonSteps
import os,sys
os.remove("delete.py")

commonSteps.generateKey()
commonSteps.encrypt_dir("./testsEnvironment", commonSteps.readKey())