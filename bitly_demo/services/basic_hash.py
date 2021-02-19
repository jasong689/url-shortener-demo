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
        existing_hash = self.repo.get_link_by_short_url(hash, self.url)

        if existing_hash is not None:
            return self.hasher.build_hash(existing_hash.hash_value, existing_hash.ver)
        else:
            current_version = self.repo.get_max_version_by_hash(hash)
            version = current_version + 1
            # user is for now simply a hard coded test user
            self.repo.create_link(hash, self.url, 'test', version)

        return hash
