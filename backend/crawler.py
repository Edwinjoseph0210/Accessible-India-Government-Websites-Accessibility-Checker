import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class WebCrawler:
    def __init__(self, base_url, max_pages=50):
        self.base_url = base_url
        self.visited = set()
        self.max_pages = max_pages
        self.pages = []

    def is_internal(self, url):
        return urlparse(url).netloc == urlparse(self.base_url).netloc

    def crawl(self, url=None):
        if url is None:
            url = self.base_url
        if url in self.visited or len(self.pages) >= self.max_pages:
            return
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                self.visited.add(url)
                self.pages.append({'url': url, 'html': resp.text})
                soup = BeautifulSoup(resp.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    next_url = urljoin(url, link['href'])
                    if self.is_internal(next_url):
                        self.crawl(next_url)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def get_pages(self):
        return self.pages

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        crawler = WebCrawler(sys.argv[1])
        crawler.crawl()
        print(f"Crawled {len(crawler.pages)} pages.")
    else:
        print("Usage: python crawler.py <base_url>") 