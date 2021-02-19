from ..models.link import Link

class UrlRepository:
    def get_url_by_short(self, short):
        link = Link.objects.get(hash_value=short)

        return link

    def create_short(self, short, url, user):
        link = Link(hash_value=short, username=user, original_url=url)
        link.save()

        return link

    def short_exists(self, short, url = None):
        try:
            link = Link.objects.get(hash_value=short, original_url=url) if url is not None else Link.objects.get(hash_value=short)
            return link.hash_value
        except Link.DoesNotExist:
            return None