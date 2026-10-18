import pytest
from django.contrib import admin
from django.urls import reverse
from posts.models import Post

def test_post_registered():
    assert Post in admin.site._registry

@pytest.mark.django_db
def test_admin_requires_login(client):
    response = client.get(reverse("admin:posts_post_changelist"))
    assert response.status_code == 302
    assert "/admin/login/" in response.url

@pytest.mark.django_db
def test_staff_can_manage_posts(admin_client):
    assert admin_client.get(reverse("admin:posts_post_changelist")).status_code == 200
