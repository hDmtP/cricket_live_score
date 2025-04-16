import requests
from bs4 import BeautifulSoup

from PIL import Image, ImageDraw, ImageFont
import time, datetime

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
venue = venue[:10]
print(venue)

series = soup.find('span', class_="text-hvr-underline text-gray").getText(separator=" ", strip=True)
print(series)

def get_date():
    x = datetime.datetime.now()
    curr_time = x.strftime("%d")+" "+x.strftime("%a")+" "+x.strftime("%H")+":"+x.strftime("%M")
    print(curr_time)
    return curr_time

def get_status():
    r = requests.get(site, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find('div', class_="cb-mtch-crd-state cb-ovr-flo cb-font-12 cb-text-apple-red").get_text(separator=" ", strip=True)
    if "toss" or "need" in data:    # faulty
        print("Live : " + data)
        return data
    data = soup.find('div', class_="cb-mtch-crd-state cb-ovr-flo cb-font-12 cb-text-complete").get_text(separator=" ", strip=True)
    if "won" in data:
        print("Completed : " + data.split()[0])
        return data
    
    return data

def get_live_score():
    r = requests.get(site, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')

    bat_data = soup.find('div', class_="cb-hmscg-bat-txt").get_text(separator=" ", strip=True)
    bwl_data = soup.find('div', class_="cb-hmscg-bwl-txt").get_text(separator=" ", strip=True)

    # data = bat_data[0] + bat_data[len(bat_data) - 13:] + "\n" + bwl_data[0] + bwl_data[len(bwl_data) - 13:]
    data = bat_data + "\n" + bwl_data
    print(data)
    return data

#oled display simulation
width, height = 128, 64  
font_size = 12
font = ImageFont.truetype("arial.ttf", font_size)
d_font_size = 10
d_font = ImageFont.truetype("arial.ttf", font_size)
s_font_size = 16
s_font = ImageFont.truetype("arial.ttf", font_size)

def show_all():
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)  
    draw.text((2, 0), venue, font=d_font, fill=255)
    draw.text((60, 0), get_date(), font=d_font, fill=255)
    draw.text((2, 15), get_live_score(), font=font, fill=255)
    draw.text((2, 50), series, font=d_font, fill=255)
    image.show()

while True:
    show_all()
    time.sleep(60)