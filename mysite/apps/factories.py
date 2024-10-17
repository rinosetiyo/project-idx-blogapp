# factories.py
import factory
from factory.django import DjangoModelFactory
from apps.models import UserProfile, Category, Post

class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.Faker('name')
    bio = factory.Faker('text', max_nb_chars=100)

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
        
    title = factory.Faker('sentence', nb_words=4)
    category_name = factory.SubFactory(CategoryFactory)
    content = factory.Faker('paragraph', nb_sentences=3)
    author = factory.SubFactory(UserProfileFactory)

# Example usage:
# books = BookFactory.create_batch(10)
# user = UserProfileFactory().create_batch(5)
# category = CategoryFactory().create_batch(5)
# post = PostFactory(author=user, category_name=category).create_batch(10)

# print(user)
# print(category)
# print(post)