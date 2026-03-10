import hashlib

def hash_file():

    file_path = input("Enter file path: ")

    with open(file_path, "rb") as f:
        data = f.read()

    hash_value = hashlib.sha256(data).hexdigest()

    print("SHA256:", hash_value)
