from django.conf.urls.defaults import *

urlpatterns = patterns('world.views',
    url(r'^$', 'home', name="home"),
)

