import requests
from bs4 import BeautifulSoup

class WebScraper:
    @staticmethod
    def scrape_text_and_links(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)

            links = set()
            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                if href.startswith("http"):
                    links.add(href)

            return text, links
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return "", set()
