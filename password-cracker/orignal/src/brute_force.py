import itertools
from src.hash_utils import hash_password

def brute_force_crack(hashed_password, algorithm, max_length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            attempt = ''.join(combination)
            if hash_password(attempt, algorithm) == hashed_password:
                return attempt
    return None
