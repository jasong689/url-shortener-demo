import hashlib
from django.conf import settings

class HashService:
    def __init__(self):
        self.hash_length = settings.HASH_LENGTH

    def hash_url(self, url):
        md5 = hashlib.md5(url.encode('utf-8')).hexdigest()
        return self.__shorten_hash(md5)

    def __shorten_hash(self, long_hash):
        return long_hash[:self.hash_length]