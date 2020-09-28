"""Register models in admin"""

from django.contrib import admin

from .models import Stage, Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    """Show stories with stage filters and orsered by date"""

    model = Story
    list_display = ("title", "stage", "date")
    list_filter = ("stage__name",)
    ordering = ("date",)


admin.site.register(Stage)
