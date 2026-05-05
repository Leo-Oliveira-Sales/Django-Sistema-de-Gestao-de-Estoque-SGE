from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


@receiver(post_save, sender=Inflow)  # Sempre que acontecer um post_save no modelo Inflow, a função update_product_quantity será executada.
def update_product_quantity(sender, instance, created, **kwargs):
    if created:  # se for criação de registro
        if instance.quantity > 0:  # se a quantidade for maior que zero
            product = instance.product  # pega o produto
            product.quantity += instance.quantity  # adiciona a quantidade no estoque
            product.save()  # salva o produto


# Sem o if, passa a permitir entradas negativas — o que pode se tornar um bug grave, pois pode reduzir o estoque de forma incorreta. O if garante que apenas entradas positivas sejam consideradas para atualização do estoque, mantendo a integridade dos dados.
