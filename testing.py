import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0",
}

site = "https://www.espncricinfo.com/"

r = requests.get(site, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')

# team1 = soup.find('p', class_="ds-text-tight-s ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3").text
# score1 = soup.find('strong', class_="ds-text-typo-mid3").text

# team2 = soup.find('p', class_="ds-text-tight-s ds-font-bold ds-capitalize ds-truncate").text
# # overs = soup.find_next('span', class_="ds-text-compact-xxs ds-mr-0.5").text
# score2 = soup.find_next('strong').text

# print(f"{team1} : {score1}")
# print(team2)
# # print(overs)
# print(score2)

# match_info = soup.find('div', class_="ds-text-compact-xxs")

venue = soup.find('span', class_="ds-text-tight-xs ds-text-typo-mid2")
score = soup.find('div', class_="ds-h-14 ds-overflow-hidden")
status = soup.find('p', class_="ds-text-tight-xs ds-font-medium ds-truncate ds-text-typo")


info = venue.get_text(separator=" ", strip=True)
scoreboard = score.get_text(separator=" ", strip=True).split()
result = status.get_text(separator=" ", strip=True)



# print(info.rsplit(maxsplit=1)[-1])
# print(" ".join(scoreboard[:2]))
# print(" ".join(scoreboard[2:]))
# print(result)

data = info.rsplit(maxsplit=1)[-1] + "\n" + " ".join(scoreboard[:2]) + "\n" + " ".join(scoreboard[2:]) + "\n" + result
print(data)