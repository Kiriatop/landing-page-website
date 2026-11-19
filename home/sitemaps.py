from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        # Вкажи name твого URL-маршруту з urls.py, наприклад 'home' або 'index'
        return ['']

    def location(self, item):
        return reverse(item)