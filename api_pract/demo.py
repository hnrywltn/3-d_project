import requests

url = "https://dog.ceo/api/breeds/list/all"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data here
    print(type(data))
else:
    print("Error: ", response.status_code)
