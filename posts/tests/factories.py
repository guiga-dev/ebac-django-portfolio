import factory
from django.contrib.auth import get_user_model
from posts.models import Post

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = factory.Sequence(lambda n: f"autor{n}")

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    title = factory.Sequence(lambda n: f"Projeto {n}")
    slug = factory.Sequence(lambda n: f"projeto-{n}")
    author = factory.SubFactory(UserFactory)
    body = "Descrição do projeto e tecnologias aplicadas."
