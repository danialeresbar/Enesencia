from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


# Proxy model
class Customer(User):
    class Meta:
        proxy = True  # No genera tabla en la base de datos

    def get_products(self):
        return list()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
