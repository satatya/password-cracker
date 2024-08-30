import hashlib

def hash_password(password, algorithm):
    """Hash a password using the specified algorithm."""
    if algorithm == 'sha224':
        return hashlib.sha224(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing algorithm")
