import unittest
import functions

# i don't have any return values for my functions, so testing via unittest is gonna be strange

# i'm mainly going to use this class to verify that all of my functions run
class TestFunctions(unittest.TestCase):
    def test_functions(self):
        self.assertTrue(functions.checkBalance(1))
        self.assertTrue(functions.changeBalance(1, True))
        self.assertTrue(functions.createAccount(1))
        self.assertTrue(functions.deleteAccount(1))
        self.assertTrue(functions.updateAccount(1, "Tuhina"))
if __name__ == '__main__':
    unittest.main()
