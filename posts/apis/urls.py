from django.conf.urls import url, include
from .views import BlogPostRudView

app_name = 'api-posts'
urlpatterns = [
   url(r'^(?P<slug>[\w-]+)$', BlogPostRudView.as_view(), name='post-rud'),
]