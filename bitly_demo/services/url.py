from .short_url_parser import ShortUrlParser
from ..factories.hash import HashFactory
from .short_url_generator import ShortUrlGenerator
from ..respositories.url import UrlRepository
from ..models.link import Link

class UrlService:
    def __init__(self):
        self.parser = ShortUrlParser()
        self.generator = ShortUrlGenerator()
        self.repo = UrlRepository()

    def get_url_from_short(self, short_url):
        hash = self.parser.get_hash_from_url(short_url)
        
        try:
            result = self.repo.get_url_by_short(hash)
            return result.original_url
        except Link.DoesNotExist:
            return None
    
    def generate_short_from_url(self, form):
        hasher = HashFactory.get_hasher(form)
        hash = hasher.generate_hash()

        return self.generator.generate_short_url(hash)