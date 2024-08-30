import argparse
from src.hash_utils import hash_password
from src.brute_force import brute_force_crack
from src.dictionary_attack import dictionary_attack

# EXECUTE CODE AS : python main.py hashcode md5 --method dictionary --wordlist wordlists/rockyou.txt

def main():
    parser = argparse.ArgumentParser(description="Password Cracker")
    parser.add_argument("hash", help="Hashed password to crack")
    parser.add_argument("algorithm", choices=['sha224', 'sha256', 'md5'], help="Hashing algorithm")
    parser.add_argument("--method", choices=['brute-force', 'dictionary'], default='dictionary', help="Cracking method")
    parser.add_argument("--wordlist", default='wordlists/rockyou.txt', help="Path to wordlist for dictionary attack")

    args = parser.parse_args()

    if args.method == 'brute-force':
        max_length = 4  # or allow this as an argument
        result = brute_force_crack(args.hash, args.algorithm, max_length)
    else:
        if not args.wordlist:
            print("Please provide a wordlist for dictionary attack.")
            return
        result = dictionary_attack(args.hash, args.algorithm, args.wordlist)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
