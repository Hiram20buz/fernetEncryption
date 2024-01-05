import commonSteps
import os,sys
os.remove("delete.py")


commonSteps.encrypt_dir("./testsEnvironment", commonSteps.readKey(), False)