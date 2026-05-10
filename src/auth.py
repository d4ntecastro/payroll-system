import hashlib


def hash_password(password):
    # SHA-256 is a standard hashing algorithm
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(stored_hash, input_password):
    return stored_hash == hash_password(input_password)
