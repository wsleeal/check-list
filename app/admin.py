from django.contrib import admin

from . import models


class RespostaAdmin(admin.StackedInline):
    model = models.Resposta
    extra = 0


@admin.register(models.Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaAdmin]


@admin.register(models.Questao)
class QuestaoAdmin(admin.ModelAdmin):
    pass
