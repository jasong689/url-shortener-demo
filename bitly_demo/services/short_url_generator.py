from django.conf import settings

class ShortUrlGenerator:
    def generate_short_url(self, hash):
        return settings.HOST + "/" + hash