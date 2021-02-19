from ..forms.basic_url import BasicUrlForm
from ..forms.custom_url import CustomUrlForm
from ..services.basic_hash import BasicHashService
from ..services.custom_hash import CustomHashService

class HashFactory:
    @staticmethod
    def get_hasher(form):
        if type(form) is BasicUrlForm:
            return BasicHashService(form.cleaned_data['url'])
        else:
            return CustomHashService(form.cleaned_data['url'], form.cleaned_data['hash'])