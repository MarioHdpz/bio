"""Story related views"""

from django.views import generic

from .models import Stage


class StagesView(generic.ListView):
    model = Stage
    context_object_name = "stages"
