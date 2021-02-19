from ..models.link import Link

class UrlRepository:
    def get_url_by_short(self, short, version):
        link = Link.objects.get(hash_value=short, ver=version)

        return link

    def create_link(self, short, url, user, version):
        link = Link(hash_value=short, username=user, original_url=url, ver=version)
        link.save()

        return link

    def get_link_by_short_url(self, short, url = None):
        try:
            link = Link.objects.get(hash_value=short, original_url=url) if url is not None else Link.objects.get(hash_value=short)
            return link
        except Link.DoesNotExist:
            return None

    def get_max_version_by_hash(self, hash):
        try:
            link = Link.objects.filter(hash_value=hash).order_by('-ver').first()
            return link.ver if link is not None else -1
        except IndexError:
            return -1