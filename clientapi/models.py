from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
