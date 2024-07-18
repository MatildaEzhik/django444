from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

def validate_username(value):
    if len(value) < 3:
        raise ValidationError('длина не должна быть меньше 3 символов')

def validate_email_not_spam(value):
    if 'spam' in value:
        raise ValidationError('эмейл не может содержать слово spam')

class User(models.Model):
    username = models.CharField(max_length=100, validators=[validate_username])
    email = models.EmailField(validators=[validate_email_not_spam])
    password = models.CharField(max_length=100)
    password_confirmation = models.CharField(max_length=100)

    def clean(self):
        if self.password != self.password_confirmation:
            raise ValidationError('пароли не совпадают')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
