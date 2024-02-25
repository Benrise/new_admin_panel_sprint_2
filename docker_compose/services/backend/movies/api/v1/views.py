from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.db.models import Q
from django.contrib.postgres.aggregates import ArrayAgg

from movies.models import Filmwork


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        qs = Filmwork.objects.prefetch_related('genres', 'persons').values().annotate(
            genres=ArrayAgg(
                'genres__name',
                distinct=True
            ),
            actors=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=Q(personfilmwork__role='actor')
            ),
            directors=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=Q(personfilmwork__role='director')
            ),
            writers=ArrayAgg(
                'persons__full_name',
                distinct=True,
                filter=Q(personfilmwork__role='writer')
            ),
        )
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
