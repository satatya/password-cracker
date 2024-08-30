# Project Overview: Password Cracker

## Objective

The goal of this project is to create a simple yet functional password cracker in Python. It demonstrates the principles of brute-force and dictionary attacks, allowing users to crack hashed passwords using various algorithms.

## Structure

- **main.py**: The entry point of the application, handling command-line arguments and invoking the appropriate cracking method.
- **src/hash_utils.py**: Contains functions to hash passwords using different algorithms.
- **src/brute_force.py**: Implements the brute-force attack by generating all possible password combinations.
- **src/dictionary_attack.py**: Implements the dictionary attack by iterating through a wordlist (e.g., `rockyou.txt`) and matching hashes.

## Usage

Refer to the [README.md](../README.md) for detailed usage instructions.

## Future Enhancements

- Add support for more hashing algorithms.
- Implement multi-threading to improve brute-force attack performance.
- Add more advanced features like rainbow tables.
