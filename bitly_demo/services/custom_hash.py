from ..validators.url import UrlValidator
from ..exceptions.hash_exists import HashExists
from ..respositories.url import UrlRepository
from ..exceptions.not_valid import NotValidException

class CustomHashService:
    def __init__(self, url, hash):
        self.url = url
        self.hash = hash
        self.validator = UrlValidator()
        self.repo = UrlRepository()
    
    def generate_hash(self):
        if not self.validator.validate(self.url):
            raise NotValidException("url not valid")

        if self.repo.short_exists(self.hash) is not None:
            raise HashExists("short url is already taken")
        else:
            self.repo.create_short(self.hash, self.url, 'test')

        return self.hash