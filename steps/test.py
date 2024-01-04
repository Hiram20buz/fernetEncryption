import commonSteps


commonSteps.generateKey()
commonSteps.encrypt_dir("./testsEnvironment", commonSteps.readKey())
commonSteps.encrypt_dir("./testsEnvironment", commonSteps.readKey(), False)
'''
commonSteps.encrypt_file("testsEnvironment/file.txt", commonSteps.readKey())
commonSteps.encrypt_file("testsEnvironment/file.txt", commonSteps.readKey(), False)
'''