from bs4 import BeautifulSoup
import pandas as pd
import requests

page = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc") 
soup = BeautifulSoup(page.content,"lxml")

title = soup.find_all("h3",class_ ="lister-item-header")
year = soup.find_all("span",class_="lister-item-year text-muted unbold")
rate = soup.find_all("div",class_ ="inline-block ratings-imdb-rating")
runtime = soup.find_all("span",class_="runtime")
genre = soup.find_all("span",class_="genre")

titles = []
years =[]
rates = []
runtimes = []
genres = []


for i in title:
    t = i.find("a").get_text()
    titles.append(t)
    
for i in year:
    years.append(i.text)

for i in rate:
    rates.append(i.text.replace("\n",""))


for i in runtime:
    runtimes.append(i.text.replace("\n",""))

for i in genre:
    genres.append(i.text.replace("\n","").strip())


df = pd.DataFrame({
    "title":titles,
    "Type":genres,
    "Year":years,
    "Duration":runtimes,
    "Rate":rates
})
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df.to_excel(writer,index=False) 