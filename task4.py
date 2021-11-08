import bs4 from BeautifulSoup
import json
import requests
def scrap_movie_details():
    dic = { }
    url = "https://www.imdb.com/title/tt0066763/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    movie_name = soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    director_name = soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").get_text()
    genres = soup.find("div" ,class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").get_text()
    data=soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")

    dic["movie_name"] = movie_name
    dic["director_name"] = [director_name]
    dic["Genres"] = genres
    # print(data)
    for i in data:
        f=i.findAll("li",class_="ipc-metadata-list__item")
        for j in f:
            if "Country" in  j.text:
                country=j.find("div",class_="ipc-metadata-list-item__content-container").text
            elif "Language" in j.text:
                language =j.findAll("a")
                for l in language:
                    dic["language"]=[l.text]
                    dic["Country"]=country
                    # print(dic)
    with open("task4.json","w") as file1:
        json.dump(dic,file1,indent=4)
    
    print(dic)

scrap_movie_details()


