# Password Cracker

This project is a simple password cracker implemented in Python. It supports both brute-force and dictionary attacks to crack hashed passwords using various algorithms.

## Features

- Supports `sha224`, `sha256`, and `md5` hashing algorithms.
- Two cracking methods: brute-force and dictionary attacks.
- Uses the popular `rockyou.txt` wordlist for dictionary attacks.

## Usage

1. Clone the repository and navigate to the project directory.

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the password cracker:
    ```bash
    python main.py <hashed_password> <algorithm> --method <method> --wordlist wordlists/rockyou.txt
    ```

    - `<hashed_password>`: The hashed password you want to crack.
    - `<algorithm>`: The hashing algorithm (`sha224`, `sha256`, `md5`).
    - `--method`: Cracking method, either `brute-force` or `dictionary`.
    - `--wordlist`: Path to the wordlist file, typically `wordlists/rockyou.txt` for dictionary attack.

## Example

```bash
python main.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 --method dictionary --wordlist wordlists/rockyou.txt
```

## License

This project is licensed under the MIT License.
