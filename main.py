from database import DataBase
from webscraper import WebScraper

if __name__ == "__main__":
    db = DataBase()
    parser = WebScraper()
    parser.run()
    print("<start> recording...")
    it = 1
    for product in parser.products:
        db.insert(product)
        print(f"{it}/{len(parser.products)}")
        it += 1
    print("<finish> recording")