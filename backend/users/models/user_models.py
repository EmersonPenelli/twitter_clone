from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=160, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    # Definindo o campo followers com related_name específico para evitar conflitos de nome
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        through="follows.Follow"
    )

    # Especificando related_name únicos para os campos `groups` e `user_permissions`
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Nome relacionado exclusivo
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Nome relacionado exclusivo
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
