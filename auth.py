import os

from helpers import Helper
from http_methods import Http

class Auth:
        
    @staticmethod
    def login(token, s3_access_key, s3_secret_key):
        try:
            email = input("Enter your email: ")
            email = Helper.yes_or_not_answer('email', email)
            # os.system("clear")
            password = input("\nEnter your password: ")
            password = Helper.yes_or_not_answer('password', password)
            
            response = Http.post('http://localhost:3000/dev/signin', {
                'email': email,
                'password': password
            }, token)
            
            token = response['token']
            s3_access_key = response['accessKeyId']
            s3_secret_key = response['secretKey']
            
            print(token, s3_access_key, s3_secret_key)
            input("ya va")
            
        except Exception as e:
            print("Error login() func => ", e)