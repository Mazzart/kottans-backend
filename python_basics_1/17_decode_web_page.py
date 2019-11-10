"""
Use the BeautifulSoup and requests Python packages to print out a list
of all the article titles on the New York Times homepage
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"


def get_and_process_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_heading(html):
    articles = []
    for article in html.find_all("div", class_="css-1ez5fsm esl82me1"):
        if article is not None and article not in articles:
            articles.append(article.get_text())

    return articles


if __name__ == "__main__":
    for article in get_heading(get_and_process_page(url)):
        print(article)
