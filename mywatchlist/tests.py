from django.test import TestCase, Client
from django.urls import resolve
from .views import show_watchlist_html, show_watchlist_xml, show_watchlist_json

# Create your tests here.
class MyWatchListAppTest(TestCase):
    def test_mywatchlist_app_url_exists(self):
        response_html = Client().get('/mywatchlist/html/')
        response_xml = Client().get('/mywatchlist/xml/')
        response_json = Client().get('/mywatchlist/json/')
        self.assertEqual(response_html.status_code, 200)
        self.assertEqual(response_xml.status_code, 200)
        self.assertEqual(response_json.status_code, 200)

    def test_mywatchlist_app_template(self):
        response = Client().get('/mywatchlist/html/')
        self.assertTemplateUsed(response, 'watchlist.html')