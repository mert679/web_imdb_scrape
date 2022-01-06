from bs4 import BeautifulSoup

import requests
import pandas as pd


page = requests.get("https://www.imdb.com/chart/top/")

soup = BeautifulSoup(page.content,"html.parser")


titleAndYear = soup.find_all("td",class_="titleColumn")
ratingOfMovie = soup.find_all("td",class_="ratingColumn imdbRating")

titles = []
years = []
ratings = [] 

for i in titleAndYear:
  title = i.find("a").get_text()
  titles.append(title)

  year = i.find(class_="secondaryInfo").get_text()
  years.append(year)



for rate in ratingOfMovie:
  rating = rate.find("strong").get_text()
  ratings.append(rating)

imbdTable = pd.DataFrame(
 {
     "Title":titles ,
     "Year": years,
     "Ratings": ratings
  }
)
print(imbdTable)
print()

def averageOfRatings(ratings):
    sum = 0
    for a in ratings:
      sum = sum + float(a)           

    avg = sum / len(ratings)
    return round(avg,4)
    
average = averageOfRatings(ratings)

print("Average rating of all: ", average) 
