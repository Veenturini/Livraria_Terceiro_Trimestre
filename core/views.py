from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Livro
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroSerializer(ModelViewSet):
    class Meta:
        model = Livro
        fields = "__all__"