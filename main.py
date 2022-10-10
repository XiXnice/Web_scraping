import bs4
import requests
from fake_headers import Headers

HUBSS = ['дизайн', 'фото', 'web', 'python', "Исследования и прогнозы в IT"]

URL = "https://habr.com/"

def req(header, url, hubss):
    response = requests.get(url, headers=header)
    text = response.text

    soup = bs4.BeautifulSoup(text, features="html.parser")

    articles = soup.find_all("article")
    for article in articles:
        hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
        hubs = [hub.text.strip() for hub in hubs]
        print(hubs)
        for hub in hubs:
            if hub in hubss:
                href = article.find(class_="tm-article-snippet__hubs-item-link").attrs["href"]
                title = article.find("h2").find("span").text
                data = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs["title"]
                result = f"{data} - {title} - {URL}{href}"
                print(result)

if __name__ == "__main__":
    HEADERS = Headers(browser="chrome", os="win", headers=True).generate()
    req(HEADERS, URL, HUBSS)
