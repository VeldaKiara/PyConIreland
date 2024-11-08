from django.urls import path
from django.views.generic import TemplateView
from atlantis.views import AtlantisListView, AtlantisDetailView, AtlantisCreateView, character_list
app_name='atlantis'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('atlantis/character/', character_list, name='character_list'),  
    path('atlantis/', AtlantisListView.as_view(), name='character-list'),
    path('atlantis/<uuid:pk>/', AtlantisDetailView.as_view(), name='character-detail'),
    path('atlantis/create/', AtlantisCreateView.as_view(), name='character-create'),
    ]

