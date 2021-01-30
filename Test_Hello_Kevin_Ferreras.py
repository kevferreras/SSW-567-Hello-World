import unittest
from Hello_Kevin_Ferreras import hello

class HelloTest(unittest.TestCase):

    def test_hello(self) -> None:
        ''' Tests that the hello function returns the message "Hello World!" '''

        message: str = hello()
        expected_message: str = "Hello World!"

        self.assertEqual(message, expected_message)

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)
