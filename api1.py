import requests
response = requests.get("https://api.venafi.cloud/v1/serverinfo")
data = response.json()
print('data')

