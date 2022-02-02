from django.test import TestCase
from django.urls import resolve 
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """"
        Vamos prosseguir escrevendo um teste para a nossa view de modo que ela 
        seja mais do que uma função que não faz nada, mas uma que devolva uma
        resposta de verdade, contendo HTML
        """
        response  = self.client.get('/')
        
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'wrong.html')