from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'app.views.home', name='home'),
)