import requests
from bs4 import BeautifulSoup
import re
from app.embeddings import process_text


def scrapping(url,website_id):
 
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
     
    for tag in soup([
    "script", "style", "noscript", "header", "footer",
    "nav", "aside", "form", "input", "button",
    "svg", "meta", "link"
]):
        tag.decompose()

    main_content = soup.find("main") or soup.find("article") or soup.find("div", id="main") or soup.body

    if not main_content:
        return ""

    content_tags = main_content.find_all(["h1", "h2", "h3", "p", "li"])
    

    texts = [tag.get_text(" ", strip=True) for tag in content_tags]

    text = " ".join(texts)

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"\s+", " ", text).strip()
    clean_text = re.sub(r"[^A-Za-z0-9\s]", "", text)




    return process_text(clean_text,website_id)
