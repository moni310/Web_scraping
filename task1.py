from bs4 import BeautifulSoup
import requests
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
res=requests.get(url)
# print(res)
soup=BeautifulSoup(res.text,"html.parser")
print(soup)
def scrap_top_list():
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    trs=tbody.find_all("tr")
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]
    for tr in trs:
        position=tr.find("td",class_="titleColumn").get_text().strip()
        rank=" "
        for i in position:
            # print(i)

            if "." not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        title=tr.find("td",class_="titleColumn").a.get_text()
        movie_name.append(title)
        year=tr.find("td",class_="titleColumn").span.get_text()
        year_of_realease.append(year)
        imdb_rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)
        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link="htts://www.imdb.com"+link
        movie_urls.append(movie_link)
    Top_movies=[]
    details={ }
    for i in range(0,len(movie_ranks)):
        details["postion"]=int(movie_ranks[i])
        details["movei_name"]=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details["year"]=int(year_of_realease[i])
        details["rating"]=float(movie_ratings[i])
        details["url"]=movie_urls[i]
        Top_movies.append(details)
        details={ }
    with open ("task1.json","w") as f:
        json.dump(Top_movies,f,indent=4)
        
    return Top_movies
pprint.pprint(scrap_top_list())
