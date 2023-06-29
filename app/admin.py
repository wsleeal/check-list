from django.contrib import admin
from django.http.request import HttpRequest


from .models import Pergunta, Resposta, Questao, Checklist


class RespostaAdmin(admin.StackedInline):
    classes = ("grp-closed",)
    inline_classes = ("grp-open",)
    model = Resposta
    extra = 0


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaAdmin]


class QuestaoAdmin(admin.StackedInline):
    classes = ("grp-open",)
    inline_classes = ("grp-open",)
    model = Questao
    extra = 0
    # readonly_fields = ["pergunta"]


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "created", "updated"]
    inlines = [QuestaoAdmin]

    def save_model(self, request: HttpRequest, obj: Checklist, form, change):
        if not change:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
