from .hash import HashService
from ..validators.url import UrlValidator
from ..respositories.url import UrlRepository
from ..exceptions.not_valid import NotValidException

class BasicHashService:
    def __init__(self, url):
        self.url = url
        self.hasher = HashService()
        self.validator = UrlValidator()
        self.repo = UrlRepository()

    def generate_hash(self):
        if not self.validator.validate(self.url):
            raise NotValidException("url not valid")

        hash = self.hasher.hash_url(self.url)
        existing_hash = self.repo.short_exists(hash, self.url)

        if existing_hash is not None:
            return existing_hash
        else:
            self.repo.create_short(hash, self.url, 'test')

        return hash
