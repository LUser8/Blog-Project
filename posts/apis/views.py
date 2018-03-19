from rest_framework import generics
from ..models import Post
from .serializers import BlogPostSerializer


class BlogPostRudView(generics.ListAPIView):
    lookup_field = 'slug'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return Post.objects.all()
