from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from atlantis.models import Character
from atlantis.serializers import CharacterSerializer

class AtlantisListView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    

class AtlantisDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class AtlantisCreateView(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
    
# def character_list(request):
#     characters = Character.objects.all()  
#     return render(request, 'character.html', {'characters': characters})

#optimized version of character_list query
def character_list(request):
    # Use select_related to fetch related Protagonist, Antagonist, and Supporting in a single query
    characters = Character.objects.select_related('protagonist', 'antagonist', 'supporting').all()
    return render(request, 'character.html', {'characters': characters})
