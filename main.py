from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key=None
        self.password=None
        self.password_dic={}

    def create_key(self, path):
        self.key = Fernet.generate_key
        with open (path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open (path, 'sb') as f:
            self.key = f.read()

    def create_password_file(self, path, inital_values=None):
        self.password_file= path

        if inital_values is not None:
            for key, value in inital_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file=path
        with open(path, 'r')as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dic[site] = Fernet(self.key).decrypt(encrypted.encode())
    
    def add_password(self, site, password):
        self.password_dic[site] = password

        if self.password_file is not None:
            with open(self.password_file, '+a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" +encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]

            