import requests
import re


class WebCrawler:
    def __init__(self):
        self.discovered_sites = []

    def crawl(self, start_url):
        que = [start_url]
        self.discovered_sites.append(start_url)

        # breadth first search
        while que:
            actual_url = que.pop(0)
            print(actual_url)
            actual_url_html = self.read_html(actual_url)
            links = self.get_links(actual_url_html)
            for url in links:
                if url not in self.discovered_sites:
                    self.discovered_sites.append(url)
                    que.append(url)

    @staticmethod
    def get_links(html) -> list:
        return re.findall(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", html)

    @staticmethod
    def read_html(url) -> str:
        try:
            html = requests.get(url).text
            return html
        except Exception as e:
            print(e)


if __name__ == '__main__':
    crawler = WebCrawler()
    crawler.crawl('https://www.cnn.com')

#
