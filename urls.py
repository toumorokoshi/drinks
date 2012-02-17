from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('Drinks.views',
    url(r'quiz','quiz'),
    url(r'search','search'),
    url(r'drink/(?P<drink_slug>.*)$','drink'),
    url(r'.*','quiz'),
)
