# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Category, Article


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_string_representation(self):
        self.assertEqual(str(self.category), 'Test Category')


class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.'
        )
        self.article.categories.add(self.category)

    def test_string_representation(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_get_absolute_url(self):
        url = reverse('article_detail', args=[str(self.article.id)])
        self.assertEqual(self.article.get_absolute_url(), url)

    def test_category_relationship(self):
        self.assertEqual(self.article.categories.count(), 1)
        self.assertEqual(self.article.categories.first(), self.category)
