from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'pint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', login, {'template_name': 'addsubs/index.html', }, name="index"),
    url(r'^$', login, {'template_name': 'addsubs/index.html', }, name="index"),
    url(r'^main$', 'addsubs.views.main', name='main'),
    url(r'^signup$', 'addsubs.views.signup', name='signup'),
    url(r'^options$', 'addsubs.views.options', name='options'),
    url(r'^jobs$', 'addsubs.views.jobs', name='jobs'),
]
