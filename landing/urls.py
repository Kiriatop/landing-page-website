"""
URL configuration for landing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}
def indexable_sitemap(request, sitemaps, **kwargs):
    response = sitemap(request, sitemaps, **kwargs)
    if "X-Robots-Tag" in response:
        del response["X-Robots-Tag"]
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("sitemap.xml",indexable_sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap")
]
