import pytest
from .factories import PostFactory
from posts.models import Post

pytestmark = pytest.mark.django_db

def test_list_shows_published_only(client):
    public = PostFactory(title="Projeto público", status=Post.Status.PUBLISHED)
    private = PostFactory(title="Rascunho privado")
    response = client.get("/")
    assert response.status_code == 200
    assert public.title.encode() in response.content
    assert private.title.encode() not in response.content
    assert {"base.html", "index.html", "post.html", "sidebar.html"}.issubset({t.name for t in response.templates})

def test_detail_and_draft_protection(client):
    post = PostFactory(status=Post.Status.PUBLISHED, body="<script>alert(1)</script>")
    response = client.get(post.get_absolute_url())
    assert response.status_code == 200
    assert b"&lt;script&gt;" in response.content
    post.status = Post.Status.DRAFT
    post.save()
    assert client.get(post.get_absolute_url()).status_code == 404
