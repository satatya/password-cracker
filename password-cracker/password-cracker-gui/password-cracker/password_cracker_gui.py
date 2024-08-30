import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import hashlib
import itertools

# Utility function to hash a password using the specified algorithm
def hash_password(password, algorithm):
    if algorithm == 'sha224':
        return hashlib.sha224(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm")

# Brute-force cracking function
def brute_force_crack(hashed_password, algorithm, max_length=4):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            attempt = ''.join(combination)
            if hash_password(attempt, algorithm) == hashed_password:
                return attempt
    return None

# Dictionary attack cracking function
def dictionary_attack(hashed_password, algorithm, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for password in file:
                password = password.strip()
                if hash_password(password, algorithm) == hashed_password:
                    return password
    except FileNotFoundError:
        return None
    return None

# Function to handle the cracking process
def crack_password():
    hashed_password = hash_entry.get()
    algorithm = algorithm_combobox.get()
    attack_type = attack_type_combobox.get()
    wordlist_path = wordlist_entry.get()
    
    result = None
    if attack_type == 'Brute-force':
        result = brute_force_crack(hashed_password, algorithm)
    elif attack_type == 'Dictionary':
        if not wordlist_path:
            messagebox.showwarning("Input Error", "Please provide a wordlist for dictionary attack.")
            return
        result = dictionary_attack(hashed_password, algorithm, wordlist_path)
    
    if result:
        result_label.config(text=f"Password found: {result}")
    else:
        result_label.config(text="Password not found.")

# Function to browse and select a wordlist file
def browse_wordlist():
    filename = filedialog.askopenfilename(title="Select Wordlist", filetypes=[("Text files", "*.txt")])
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, filename)

# Initialize the GUI
root = tk.Tk()
root.title("Password Cracker")

# Hash entry
ttk.Label(root, text="Hashed Password:").grid(column=0, row=0, padx=10, pady=10)
hash_entry = ttk.Entry(root, width=40)
hash_entry.grid(column=1, row=0, padx=10, pady=10)

# Algorithm selection
ttk.Label(root, text="Hashing Algorithm:").grid(column=0, row=1, padx=10, pady=10)
algorithm_combobox = ttk.Combobox(root, values=['sha224', 'sha256', 'md5'], state='readonly')
algorithm_combobox.grid(column=1, row=1, padx=10, pady=10)
algorithm_combobox.current(0)

# Attack type selection
ttk.Label(root, text="Attack Type:").grid(column=0, row=2, padx=10, pady=10)
attack_type_combobox = ttk.Combobox(root, values=['Brute-force', 'Dictionary'], state='readonly')
attack_type_combobox.grid(column=1, row=2, padx=10, pady=10)
attack_type_combobox.current(1)

# Wordlist entry for dictionary attack
ttk.Label(root, text="Wordlist (for Dictionary Attack):").grid(column=0, row=3, padx=10, pady=10)
wordlist_entry = ttk.Entry(root, width=40)
wordlist_entry.grid(column=1, row=3, padx=10, pady=10)
browse_button = ttk.Button(root, text="Browse", command=browse_wordlist)
browse_button.grid(column=2, row=3, padx=10, pady=10)

# Crack button
crack_button = ttk.Button(root, text="Crack Password", command=crack_password)
crack_button.grid(column=1, row=4, padx=10, pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
