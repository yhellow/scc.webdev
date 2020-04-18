import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
r = requests.get(
    "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303",
    headers=headers,
)

soup = BeautifulSoup(r.text, "html.parser")

# 영화 나열
# old_content 라는 아이디 속 table - tbody - tr 태그를 타고 들어간다
movies = soup.select("#old_content>table>tbody>tr")


rank = 1
for movie in movies:
    #     # select_one을 해주는 이유는 하나씩 돌아가며 반복문을 돌려주는 것이기 때문
    movname = movie.select_one("td.title>div>a")
    if movname is not None:
        title = movname.text
        rate = movie.select_one("td.point").text
        print (rank, title, rate)
        rank += 1
