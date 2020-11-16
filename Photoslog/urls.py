from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^search/', views.search_photo, name='search_photo'),
    url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single_image,name = 'single_image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)