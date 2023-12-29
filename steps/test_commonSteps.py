import unittest
import commonSteps
import os

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
class TestCommonSteps(unittest.TestCase):

    def test_generateKey(self):
        commonSteps.generateKey()
        self.assertTrue(os.path.exists("thekey.key"))
        
    def test_readKey(self):
        self.assertIsNotNone(commonSteps.readKey())

    def test_encrypt_file(self):
        commonSteps.generateKey()
        key = commonSteps.readKey()
        a = open("testsEnvironment/file.txt").read()
        commonSteps.encrypt_file("testsEnvironment/file.txt", key)
        b = open("testsEnvironment/file.txt").read()
        self.assertNotEqual(a, b)
        commonSteps.encrypt_file("testsEnvironment/file.txt", key, False)
        c = open("testsEnvironment/file.txt").read()
        self.assertEqual(a, c)
        


if __name__ == '__main__':
    unittest.main()