from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'pint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('addsubs.urls')),
    url(r'^$', include('addsubs.urls')),
    url(r'^$', 'addsubs.views.main', name='main'),
    url(r'^signup$', 'addsubs.views.signup', name='signup'),
]
