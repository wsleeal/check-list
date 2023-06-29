from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
from django.db.models import signals
from django.dispatch import receiver


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.pergunta


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.resposta


class Checklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class Questao(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = ChainedForeignKey(Resposta, null=True, chained_field="pergunta", chained_model_field="pergunta")


@receiver(signals.post_save, sender=Checklist)
def populate_checklist(sender, instance: Checklist, **kwargs):
    perguntas = Pergunta.objects.all()
    for pergunta in perguntas:
        q = Questao(pergunta=pergunta, checklist=instance)
        q.save()
