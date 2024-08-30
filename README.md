# Password Cracker

This project is a Python-based password cracker that demonstrates the effectiveness of brute-force and dictionary attacks against hashed passwords. It includes a command-line interface (CLI) as well as a graphical user interface (GUI) built with `tkinter`.

## Features

- Supports `sha224`, `sha256`, and `md5` hashing algorithms.
- Two cracking methods:
  - **Brute-force Attack**: Tries all possible combinations of characters.
  - **Dictionary Attack**: Uses a precompiled wordlist, such as `rockyou.txt`.
- GUI interface for easy interaction.
- Command-line interface for advanced usage.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
  - [Graphical User Interface](#graphical-user-interface)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password-cracker.git
   cd password-cracker
2.	Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
3.	Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
4.	Download the rockyou.txt wordlist (if you don't have it already):
Usage
Command-Line Interface
You can run the password cracker directly from the command line using main.py.
bash
Copy code
python main.py <hashed_password> <algorithm> --method <method> --wordlist <path_to_wordlist>
•	<hashed_password>: The hashed password you want to crack.
•	<algorithm>: The hashing algorithm (sha224, sha256, md5).
•	--method: The cracking method, either brute-force or dictionary.
•	--wordlist: Path to the wordlist file (required for dictionary attack).
Example:
python main.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 --method dictionary --wordlist wordlists/rockyou.txt
Graphical User Interface
The project also includes a tkinter-based GUI for easier interaction.
python password_cracker_gui.py

1.	Enter the hashed password.
2.	Select the hash algorithm.
3.	Choose the attack type (brute-force or dictionary).
4.	For dictionary attacks, specify the path to the wordlist.
5.	Click "Crack Password" to begin.

## Testing
Unit tests are provided in the tests/ directory. You can run these tests using the unittest framework.


python -m unittest discover tests
Project Structure
plaintext
Copy code
password-cracker/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── main.py
├── password_cracker_gui.py
├── wordlists/
│   └── rockyou.txt
├── src/
│   ├── __init__.py
│   ├── hash_utils.py
│   ├── brute_force.py
│   └── dictionary_attack.py
├── tests/
│   ├── __init__.py
│   ├── test_hash_utils.py
│   ├── test_brute_force.py
│   └── test_dictionary_attack.py
└── docs/
    ├── project_report.docx
    └── project_overview.md

