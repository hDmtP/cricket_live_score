import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

site = "https://www.espncricinfo.com/"

r = requests.get(site, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

match_link = soup.find('a', class_="ds-no-tap-higlight")

if match_link:
    url = match_link.get("href")
    site += url
    print(site)

# ds-w-full ds-table ds-table-md ds-table-auto  # table
# ds-text-right # tbody

r = requests.get(site, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

stats = soup.find('table', class_="ds-w-full ds-table ds-table-md ds-table-auto")

print(stats.get_text(separator=" ", strip=True))