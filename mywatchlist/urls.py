from django.urls import path
from mywatchlist.views import show_watchlist_html, show_watchlist_xml, show_watchlist_json
from mywatchlist.views import show_json_by_id, show_xml_by_id

app_name = 'watchlist'

urlpatterns = [
    path('html/', show_watchlist_html, name='show_watchlist_html'),
    path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
    path('json/', show_watchlist_json, name='show_watchlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]