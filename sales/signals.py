from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Product

from django.db.models.signals import pre_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Product

@receiver(pre_save, sender=Product)
def product_availability_changed(sender, instance, **kwargs):
    print("SIGNAL CALLED")

    if not instance.pk:
        print("SKIP: new object")
        return

    try:
        old = Product.objects.get(pk=instance.pk)
        print("OLD:", old.availability, "NEW:", instance.availability)
    except Product.DoesNotExist:
        return

    channel_layer = get_channel_layer()

    if old.availability and not instance.availability:
        print("AVAILABLE → UNAVAILABLE")

        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "data": {
                    "event": "PRODUCT_UNAVAILABLE",
                    "product_id": instance.pk,
                    "product_name": instance.name,
                    "message": f"{instance.name} is not available"
                }
            }
        )

    elif not old.availability and instance.availability:
        print("UNAVAILABLE → AVAILABLE")

        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "notify",
                "data": {
                    "event": "PRODUCT_AVAILABLE",
                    "product_id": instance.pk,
                    "product_name": instance.name,
                    "message": f"{instance.name} is now available"
                }
            }
        )

    else:
        print("NO CHANGE")



@receiver(post_save, sender=Product)
def product_availability_notify(sender, instance, created, **kwargs):
    print("SIGNAL FIRED", instance.id, instance.availability)
