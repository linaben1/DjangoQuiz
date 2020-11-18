import django_filters
from .models import *


class imageFilter(django_filters.FilterSet):
    class Meta:
        model = image
        fields = '__all__'
