from django.conf.urls import patterns, include, url
from django.contrib import admin
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kevin_liao_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'), 
    url(r'^index/', views.index, name='index'), 
    url(r'^$', views.index, name='index'), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), 
) 
