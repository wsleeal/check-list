from collections.abc import Sequence
from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest


from .models import *


class RespostaAdmin(admin.StackedInline):
    model = Resposta
    extra = 0


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaAdmin]


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request)


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "created", "updated"]

    def save_model(self, request: HttpRequest, obj: Checklist, form, change):
        if not change:
            obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_delete_permission(self, request: HttpRequest, obj=None):
        if request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)
