import unittest
from src.brute_force import brute_force_crack

class TestBruteForce(unittest.TestCase):

    def test_brute_force_crack(self):
        hashed_password = '5f4dcc3b5aa765d61d8327deb882cf99'  # MD5 for 'password'
        self.assertEqual(brute_force_crack(hashed_password, 'md5', max_length=8), 'password')

if __name__ == '__main__':
    unittest.main()
