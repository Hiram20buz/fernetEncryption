import commonSteps


commonSteps.generateKey()
commonSteps.encrypt_dir("./testsEnvironment", commonSteps.readKey())
commonSteps.decrypt_dir("./testsEnvironment", commonSteps.readKey())
'''
commonSteps.encrypt_file("testsEnvironment/file.txt", commonSteps.readKey())
commonSteps.decrypt_file("testsEnvironment/file.txt", commonSteps.readKey())
'''