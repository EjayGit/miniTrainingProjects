from bs4 import BeautifulSoup

with open("home.html") as file:
    content = file.read()

newSoup = BeautifulSoup(content,"html.parser")
print(newSoup.prettify())
print(newSoup.title)
print(newSoup.title.string)
print(newSoup.li)
print(newSoup.li.string)
print(newSoup.a)
print(newSoup.p)

anchorTags = newSoup.find_all(name="a")
print(anchorTags)
for tag in anchorTags:
    print(tag.getText())
paraTags = newSoup.find_all(name="p")
print(paraTags)

h1 = newSoup.find_all(name="h1", id="name")
for header in h1:
    print(header.getText())

h3 = newSoup.find_all(name="h3", class_='heading')
for header in h3:
    print(header.get("class"))

anchors = newSoup.find_all(name="a")
for anchor in anchors:
    print(anchor.get("href"))

appmillersURL = newSoup.select_one(selector="p a") # mean anchor tag inside para tag
print(appmillersURL)
print(appmillersURL.get("href"))

tag = newSoup.select_one(selector=".heading") # looking for class name heading => .heading
print(tag)