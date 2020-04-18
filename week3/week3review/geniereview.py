import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
# 정확히 headers의 역할이 뭔지 모르겠음
r = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')



songs = soup.select('div.music-list-wrap>table>tbody>tr')

rank = 1
for song in songs:
    titletag = song.select_one('td.info > .title')
    title = titletag.text.lstrip()
    
    artisttag = song.select_one('td.info > .artist')
    artist = artisttag.text

    print(rank, ' ',title, ' ', artist)
    rank += 1




