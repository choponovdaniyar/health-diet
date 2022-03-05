import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import re

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers["user-agent"] = UserAgent().random
        self.products = list()
        self.__catalog_links = list()

    def __get_html(self,url):
        return BeautifulSoup(self.session.get(url).text, "lxml")


    def __collection_products(self, url):
        soup = self.__get_html(url)
        table = soup.find("tbody").find_all("tr")
        for row in table:
            row = tuple(x.text.strip() for x in row.find_all("td"))
            if len(row) == 5:
                self.products.append(row)
            else:
                break
            

    def __collection_catalogs(self, url="https://health-diet.ru/table_calorie/"):
        soup = self.__get_html(url)
        all_links = soup.find_all("a", class_="mzr-tc-group-item-href")
        for link in all_links:
            try:
                link = link.attrs["href"]
                if re.search(r'^/base_of_food/food_[0-9]+/$',link):
                    self.__catalog_links.append(f"https://health-diet.ru{link}")
            except KeyError:
                continue


    def run(self):
        self.__collection_catalogs()
        size = len(self.__catalog_links)
        it = 0
        for link in self.__catalog_links:
            self.__collection_products(link)
            it += 1
            print(f"{it}/{size}")   


if __name__ == "__main__":
    parser = WebScraper()
    parser.run()