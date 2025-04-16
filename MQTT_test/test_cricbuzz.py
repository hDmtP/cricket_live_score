import requests
from bs4 import BeautifulSoup
import time

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
site2 = site + data
print(site2)
r = requests.get(site2, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
venue = soup.find('span', itemprop="addressLocality").getText(separator=" ", strip=True)
print(venue)

def get_toss():
    r = requests.get(site, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find('div', class_="cb-mtch-crd-state cb-ovr-flo cb-font-12 cb-text-complete").get_text(separator=" ", strip=True)
    if "toss" in data:
        print(data.split()[0])
        return f"T : {data.split()[0]}"
    return "T : "

def get_win():
    r = requests.get(site, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find('div', class_="cb-mtch-crd-state cb-ovr-flo cb-font-12 cb-text-complete").get_text(separator=" ", strip=True)
    if "by" in data:
        print(data.split()[0])
        return f"W : {data.split()[0]}"
    return "W : "


site = "https://www.cricbuzz.com/"

def get_live_score():
    r = requests.get(site, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')

    # div = soup.find('li', class_="cb-view-all-ga cb-match-card cb-bg-white")
    # if div:
    #     score = div.find('a')
    #     if score:
    #         scoreboard = score.get_text(separator=" ", strip=True)

    # print(scoreboard)
    
    score = (soup.find('div', class_="cb-hmscg-bat-txt").get_text(separator=" ", strip=True))
    score += '\n\n'
    score += (soup.find('div', class_="cb-hmscg-bwl-txt").get_text(separator=" ", strip=True))
    return score
    # print(soup.find('div', class_="cb-mtch-crd-state cb-ovr-flo cb-font-12 cb-text-complete").get_text(separator=" ", strip=True))

# get_toss()
get_live_score()
# get_win()