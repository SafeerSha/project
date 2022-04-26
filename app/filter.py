import django_filters
from.models import shop

class itemFilter (django_filters.FilterSet):
    class Meta:
        models = shop
        fields = [
            'product'
            , 'state',
            'catergory',
        ]