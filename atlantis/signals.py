# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Character

# @receiver(post_save, sender=Character)
# def character_post_save(sender, instance, created, **kwargs):
#     if created:
#         # Perform actions only when a new character is created
#         # Avoid heavy computations or unnecessary queries here
#         print(f"New character created: {instance.name}")