import pyrebase
from CABScraper import CABScraper

"""Script used to scrape CAB for current information, and push said scraped
information to firebase realtime database under the 'scraped courses' node."""

JSON_PATH = "/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/python/Scraper/cabscraper/spiders/data_edited.json"
firebaseConfig = {
        "apiKey": "AIzaSyD48KcKMMV5oiuXyDqXNcLyXDPBxPLQWNc",
        "authDomain": "tabsoncab.firebaseapp.com",
        "databaseURL": "https://tabsoncab-default-rtdb.firebaseio.com",
        "storageBucket": "tabsoncab.appspot.com",
        "serviceAccount": "/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/tabsoncab-firebase-adminsdk-21dok-3040407482.json"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
scraper = CABScraper()
scraped_data = scraper.scrape(scraper.department_codes)
db.child("scraped courses").set(scraped_data)