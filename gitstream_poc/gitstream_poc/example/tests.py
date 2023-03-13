# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Article
from .forms import ArticleForm


class ArticleCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('article_create')
        self.data = {
            'title': 'Test Article',
            'content': 'This is a test article.'
        }

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_form.html')
        self.assertIsInstance(response.context['form'], ArticleForm)

    def test_post_valid(self):
        response = self.client.post(self.url, data=self.data)
        self.assertRedirects(response, reverse('article_list'))
        self.assertEqual(Article.objects.count(), 1)
        article = Article.objects.first()
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.content, 'This is a test article.')

    def test_post_invalid(self):
        data = {'title': '', 'content': ''}
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_form.html')
        self.assertIsInstance(response.context['form'], ArticleForm)
        self.assertContains(response, 'This field is required.')
