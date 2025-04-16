import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0",
}

site = "https://www.cricbuzz.com"

r = requests.get(site, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

data = soup.find('li', class_="cb-view-all-ga cb-match-card cb-bg-white").find('a')["href"]

site = site + data

print(site)

r = requests.get(site, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

venue = soup.find('span', itemprop="addressLocality").getText(separator=" ", strip=True)
print(venue)

scoreboard = soup.find('div', class_="cb-col-67 cb-col").getText(separator=" ", strip=True)
print(scoreboard)