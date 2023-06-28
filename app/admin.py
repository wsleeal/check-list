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
    readonly_fields = ["user_str", "user_obj"]

    def save_model(self, request: HttpRequest, obj: Checklist, form, change) -> None:
        obj.user_str = 1234
        obj.user_obj = request.user
        return super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request: HttpRequest, obj=None) -> Sequence[str]:
        return super().get_readonly_fields(request, obj)
