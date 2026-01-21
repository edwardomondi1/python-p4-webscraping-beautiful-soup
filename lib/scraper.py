from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

print("Status code:", html.status_code)

doc = BeautifulSoup(html.text, 'html.parser')

# Check if the text is in the HTML
