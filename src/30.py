import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(e)

url = "https://api.example.com/data"
data = fetch_data(url)
print(data)
