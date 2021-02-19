from ..forms.basic_url import BasicUrlForm
from ..forms.custom_url import CustomUrlForm

class FormFactory:
    @staticmethod
    def get_form(post_data):
        hash = post_data.get("hash", "")

        return CustomUrlForm(post_data) if hash != "" else BasicUrlForm(post_data)