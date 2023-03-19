from bs4 import BeautifulSoup
import requests


def get_articles():
    articles = []
    response = requests.get(url="https://news.ycombinator.com/news")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article_titles = [(title.a.string, title.a["href"]) for title in soup.select('td.title span.titleline')]
    article_upvotes = [int(upvote.select_one("span.subline span.score").string.split(" ")[0])
                       if upvote.select_one("span.subline span.score") else None for upvote in
                       soup.select('td.subtext')]

    for i in range(len(article_titles)):
        title, link = article_titles[i]
        upvote = article_upvotes[i]
        articles.append({
            "title": title,
            "link": link,
            "upvote": upvote
        })

    return articles


with open("website.html") as df:
    contents = df.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.em.strong)


all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading[0].get("class"))

# Use CSS Selector to select tag
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)


headings = soup.select(".heading")
print(headings)




