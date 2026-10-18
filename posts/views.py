from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")
