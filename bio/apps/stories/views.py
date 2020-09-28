"""Story related views"""

from django.views import generic

from .models import Stage


class StagesView(generic.ListView):
    """List all stages in order"""

    queryset = Stage.objects.all().order_by("position")
    context_object_name = "stages"
