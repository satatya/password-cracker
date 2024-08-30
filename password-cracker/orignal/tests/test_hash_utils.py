import unittest
from src.hash_utils import hash_password

class TestHashUtils(unittest.TestCase):

    def test_md5(self):
        self.assertEqual(hash_password('password', 'md5'), '5f4dcc3b5aa765d61d8327deb882cf99')

    def test_sha256(self):
        self.assertEqual(hash_password('password', 'sha256'), '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd6a8fe317d9a7a0d74')

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            hash_password('password', 'unsupported')

if __name__ == '__main__':
    unittest.main()
