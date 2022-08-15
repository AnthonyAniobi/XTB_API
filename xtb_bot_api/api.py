import requests

class Client:
    __url__ = 

    def login(email:str, password:str, appName:str):
        _headers = {
	"command": "login",
	"arguments": {
		"userId": "1000",
		"password": "PASSWORD",
		"appId": "test",
		"appName": "test"
	}
}
        requests.get(url='', headers=_headers)