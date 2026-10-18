from django.contrib import admin
from django.urls import path
from posts.views import home, PostListView, PostDetailView

urlpatterns = [
    path("admin/", admin.site.urls), path("home", home, name="home"),
    path("", PostListView.as_view(), name="post-list"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
]
