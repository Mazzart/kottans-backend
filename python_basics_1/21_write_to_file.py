"""
Take the code from the How To Decode A Website exercise and
instead of printing the results to a screen, write the results to a txt file.

Extras:
Ask the user to specify the name of the output file that will be saved.
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
    file_name = input("Enter the name of file to which save info: ")
    for article in get_heading(get_and_process_page(url)):
        with open(f"{file_name}.txt", "a") as file:
            file.write(article)
            file.write('\n')
