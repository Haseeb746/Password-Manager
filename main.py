from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key=None
        self.password=None
        self.password_dic={}

    def create_key(self, path):
        self.key = Fernet.generate_key()
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
    
def main():
    password ={
        "email": "123456",
        "Twitter": "Haseeb123",
        "Instagram": "Goku123"
    }
    pm = PasswordManager
    print("How can I help you today? \n(1) Create a new key \n(2) Load an existing key \n(3) Create new password file \n(4) Load existing password file \n(5)add a new password \n(6)Get a password \n(q)Quit program")
    
    done = False

    while not done:
        choice = input("Enter what you would like to do: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
    
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)

        elif choice == '3':
            path = input ("Enter path: ")
            pm.create_password_file(path)
        
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)

        elif choice == "5":
            site = input("Enter the website: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        
        elif choice =="6":
            site = input("What website do you want: ")
            print(f"password for {site} is {pm.get_password(site)}")

        elif choice == "q":
            done = True
            print("Thank you for using my program, Have a great day!")
        
        else:
            print("Invalid choice, please try again.")
        
if __name__ =="__main__":
    main()