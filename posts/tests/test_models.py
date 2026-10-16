import pytest
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError
from posts.models import Post
from .factories import PostFactory

pytestmark = pytest.mark.django_db

def test_post_saved_and_defaults():
    post = PostFactory()
    restored = Post.objects.get(pk=post.pk)
    assert str(restored) == post.title
    assert restored.status == Post.Status.DRAFT
    assert restored.author.posts.get() == restored
    assert restored.created_at and restored.updated_at

def test_slug_is_unique():
    PostFactory(slug="unico")
    with pytest.raises(IntegrityError), transaction.atomic():
        PostFactory(slug="unico")

def test_title_is_required_and_validated():
    post = PostFactory.build(title="")
    with pytest.raises(ValidationError):
        post.full_clean(exclude=["author"])

def test_delete_author_cascades_posts():
    post = PostFactory()
    post.author.delete()
    assert not Post.objects.filter(pk=post.pk).exists()
