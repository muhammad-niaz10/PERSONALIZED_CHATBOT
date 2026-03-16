from app.database import get_db
from app.models import Websites
from app.scraper import scrapping

db = next(get_db())

websites = db.query(Websites).all()

for site in websites:

    print("Processing:", site.url)

    scrapping(site.url, site.id)

print("All websites embedded successfully")