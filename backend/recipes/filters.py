import django_filters
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    tags = django_filters.AllValuesMultipleFilter(
        field_name='tags__slug',
        lookup_expr='exact'
    )
    is_in_shopping_cart = django_filters.BooleanFilter(
        method='filter_shopping_cart'
    )
    is_favorited = django_filters.BooleanFilter(
        method='filter_favorited'
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags']

    def filter_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(shopping_carts__user=user)
        return queryset

    def filter_favorited(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(favorites__user=user)
        return queryset
    