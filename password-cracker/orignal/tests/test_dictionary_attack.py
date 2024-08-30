import unittest
from src.dictionary_attack import dictionary_attack

class TestDictionaryAttack(unittest.TestCase):

    def test_dictionary_attack(self):
        hashed_password = '5f4dcc3b5aa765d61d8327deb882cf99'  # MD5 for 'password'
        result = dictionary_attack(hashed_password, 'md5', 'wordlists/rockyou.txt')
        self.assertEqual(result, 'password')

if __name__ == '__main__':
    unittest.main()
