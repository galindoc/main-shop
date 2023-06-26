from django.contrib import admin

from src.apps.sections.forms import ContentForm
from src.apps.sections.models import (
    ContentText,
    Button,
    ContentImage,
    Content,
    Section,
)


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 0


class ContentTextAdmin(admin.ModelAdmin):
    model = ContentText
    inlines = [
        ButtonInline,
    ]


class ContentImageAdmin(admin.ModelAdmin):
    model = ContentImage


class ContentInline(admin.StackedInline):
    model = Content
    extra = 0
    form = ContentForm


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [
        ContentInline,
    ]

admin.site.register(Section, SectionAdmin)
admin.site.register(ContentText, ContentTextAdmin)
admin.site.register(ContentImage, ContentImageAdmin)
