from src.hash_utils import hash_password

def dictionary_attack(hashed_password, algorithm, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for password in file:
                password = password.strip()
                if hash_password(password, algorithm) == hashed_password:
                    return password
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_path}' not found.")
        return None
    return None
