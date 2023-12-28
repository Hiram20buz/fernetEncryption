import unittest
import commonSteps
import os


class TestCommonSteps(unittest.TestCase):

    def test_generateKey(self):
        commonSteps.generateKey()
        self.assertTrue(os.path.exists("thekey.key"))
