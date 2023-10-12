from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()


class SubMenuItem(models.Model):
    parent_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
