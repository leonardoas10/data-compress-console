import os
from auth import Auth

class Console:
    def __init__(self):
        self.power: bool = True
        self.token: str = ''
        self.s3_access_key: str = ''
        self.s3_secret_key: str = ''
        
    def run(self):
        try:
            # Ascii.start()
            print('DATA COMPRESS CONSOLE!')
            options = input(' Elije una opcion: 1. Login 2. Logout 3. Exit => ')
            
            while self.power:
                if options.isnumeric():
                    print(options)
                    os.system("clear")
                    if int(options) == 1:
                        Auth.login(self.token, self.s3_access_key, self.s3_secret_key)
                    else:
                        os.system("clear")
                        print("Please choose an valid option")
                else:
                    os.system("clear")
                    print("You must enter a number")
                    self.power = False
        except (Exception, ValueError):
            print()
        
if __name__ == '__main__':
    console = Console()
    console.run()