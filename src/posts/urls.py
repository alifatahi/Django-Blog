# so we use urls module to declare url
from django.conf.urls import url
# we use . to import views
from . import views

# Declare our urls in list
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    # Regular Expression using for our id:
    # P = parameter , <id> = is identifier , \d + = is means digit and also + number not -
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='post_delete'),
]
