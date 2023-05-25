from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.CharField(max_length=100, unique=True)
    string = models.CharField(max_length=100)
    is_palindrome = models.BooleanField(default=False)

    def __str__(self):
        return self.game_id