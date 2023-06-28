from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.pergunta


class Resposta(models.Model):
    resposta = models.CharField(max_length=200)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.resposta


class Questao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = ChainedForeignKey(Resposta, chained_field="pergunta", chained_model_field="pergunta")

    def __str__(self) -> str:
        return "{} - {}".format(self.id, str(self.pergunta).upper())


class Checklist(models.Model):
    user_str = models.CharField(null=True, blank=True, max_length=200)
    user_obj = models.ForeignKey(User, on_delete=models.CASCADE)
