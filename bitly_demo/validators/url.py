from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class UrlValidator:
    def validate(self, url):
        try:
            val = URLValidator(schemes=['http', 'https'])
            val(url)

            return True
        except ValidationError as e:
            return False