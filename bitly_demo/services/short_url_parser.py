from urllib.parse import urlparse

class ShortUrlParser:
    def get_hash_from_url(self, url):
        parsed = urlparse(url)

        return parsed.path[1:]