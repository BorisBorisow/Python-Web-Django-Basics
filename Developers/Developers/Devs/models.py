from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)

    # за да ни се показват обектите с конкретни имета правим стр функция, задаваща какво да изобразява
    def __str__(self):
        return self.first_name + " " + self.second_name
