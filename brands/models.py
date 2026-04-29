from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Salva a datat do momento da criação
    updated_at = models.DateTimeField(auto_now=True)  # Salva a data do momento da criação/modificação

    class Meta:
        ordering = ["name"]  # Ordenar por nome

    def __str__(self):
        return self.name
