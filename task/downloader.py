import requests

def download(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
