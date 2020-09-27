"""Register models in admin"""

from django.contrib import admin

from .models import Stage, Story


class InlineStory(admin.StackedInline):
    """Allow to edit stories inline"""

    model = Story


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    """Stage register"""

    inlines = [InlineStory]
