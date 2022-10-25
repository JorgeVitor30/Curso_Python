from bs4 import BeautifulSoup
import requests


URL = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(URL)
html = BeautifulSoup(response.text, 'html.parser')

print(response.text)
