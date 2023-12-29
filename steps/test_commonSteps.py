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


if __name__ == '__main__':
    unittest.main()