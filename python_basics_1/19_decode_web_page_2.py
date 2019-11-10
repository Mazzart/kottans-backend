"""
Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"


def get_and_process_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_article(html):
    article = []
    for text in html.find_all("p"):
        article.append(text.text)

    return article


if __name__ == "__main__":
    article = get_article(get_and_process_page(url))
    for text in article:
        print(text, '\n')
