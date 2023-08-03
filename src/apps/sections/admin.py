from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from src.apps.sections.forms import ButtonForm
from src.apps.sections.models import (
    Button,
    SingleImageContent,
    DoubleImageContent,
    Section,
)


class ButtonAdminInline(admin.StackedInline):
    form = ButtonForm
    model = Button
    extra = 0


class ButtonLeftAdminInline(admin.StackedInline):
    form = ButtonForm
    model = Button
    fk_name = 'content_left'
    extra = 0


class ButtonRightAdminInline(admin.StackedInline):
    form = ButtonForm
    model = Button
    fk_name = 'content_right'
    extra = 0


class SingleImageContentAdmin(admin.ModelAdmin):
    model = SingleImageContent
    inlines = [
        ButtonAdminInline,
    ]


class DoubleImageContentAdmin(admin.ModelAdmin):
    model = DoubleImageContent
    inlines = [
        ButtonLeftAdminInline,
        ButtonRightAdminInline,
    ]


class SectionAdmin(SortableAdminMixin ,admin.ModelAdmin):
    model = Section
    list_display = ('sort_order', 'id', 'double_image_content', 'single_image_content', 'section_type', 'active')
    ordering = ('sort_order',)

admin.site.register(Section, SectionAdmin)
admin.site.register(SingleImageContent, SingleImageContentAdmin)
admin.site.register(DoubleImageContent, DoubleImageContentAdmin)
