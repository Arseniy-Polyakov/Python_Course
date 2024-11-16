import re
import requests 
from bs4 import BeautifulSoup

url = "https://yocket.com/blog/the-10-top-universities-in-uk-to-consider-for-2023-2024-intake"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

universities_text = soup.text
universities_final = re.sub(r"[^A-Za-z0-9-\.\!\? ]", " ", universities_text)

with open("files/universities_final.txt", "wt", encoding="utf-8") as file:
    file = file.write(universities_final)
