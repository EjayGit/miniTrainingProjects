import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/?tab=hot"
response = requests.get(url)
#print(response)
#print(response.text)
stackoverflow = response.text

newSoup = BeautifulSoup(stackoverflow,"html.parser")
#print(newSoup.prettify())
#print(newSoup.title)

questionTag = newSoup.find_all(name="h3", class_="s-post-summary--content-title")
#print(questionTag)
#print(questionTag.getText())
for question in questionTag:
    questionLink = question.find(name="a").getText()
    print(questionLink)
questionVotes = newSoup.find_all(class_="s-post-summary--stats-item s-post-summary--stats-item__emphasized")
for questionVote in questionVotes:
    question = questionVote.find(class_="s-post-summary--stats-item-number").getText()
    print(question)
