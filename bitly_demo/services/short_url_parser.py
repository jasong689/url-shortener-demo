from urllib.parse import urlparse

class ParseResult:
    def __init__(self, hash, version = None):
        self.hash = hash
        self.version = version

class ShortUrlParser:
    def get_hash_from_url(self, url):
        parsed = urlparse(url)
        hash = parsed.path[1:]

        if len(hash) > 6:
            return ParseResult(hash[0:5], hash[6:])
        else:
            return ParseResult(hash, 0)