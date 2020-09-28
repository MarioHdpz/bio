"""Story related views"""

from django.views import generic

from .models import Stage, Story


class StagesView(generic.ListView):
    """List all stages in order"""

    queryset = Stage.objects.all().order_by("position")
    context_object_name = "stages"


class StoriesListView(generic.ListView):
    """List stories for each stage"""

    context_object_name = "stories"

    def get_queryset(self):
        """Return stage stories ordered by date"""
        slug = self.kwargs.get("slug")
        queryset = Story.objects.filter(stage__slug=slug)
        return queryset.order_by("date")
