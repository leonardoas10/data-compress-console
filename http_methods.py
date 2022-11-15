import requests

class Http:
    @staticmethod
    def post(url: str, json, token: str):
        try:
            response = requests.post(url, json=json, headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(token)})
            return response.json()
        except Exception as e:
            print("Error post() func => ", e)