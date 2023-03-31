from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key=None
        self.password=None
        self.password={}

def create_key(self, path):
    self.key = Fernet.generate_key
    with open (path, 'wb') as f:
        f.write(self.key)

def load_key(self, path):
    with open (path, 'sb') as f:
        self.key = f.read()