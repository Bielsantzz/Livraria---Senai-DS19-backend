import django_filters as df
from django.db.models import Q
from .models import Autor, Livro

class LivroFilter(df.FilterSet):
    id = df.NumberFilter(field_name= 'id',lookup_expr='exact')
    titulo = df.CharFilter(field_name='titulo', lookup_expr='icontains')
    Autor = df.CharFilter(method='filter_autor')

    def filter_autor(self, qs, name, value):
        if not value:
            return qs
        return qs.filter(Q(Autor__nome__icontains=value) | Q(Autor__sobrenome__icontains=value)) 

    class Meta:
        model = Livro
        fields = []