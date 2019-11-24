from django.db import models


class World(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "world"
        verbose_name_plural = "worlds"
        db_table = "worlds"

    def __str__(self):
        return "World: {}".format(self.name)


class Image(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField()
    consultation_data = models.DateTimeField(auto_now_add=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        db_table = "images"

    def __str__(self):
        return "{} world image".format(self.world.name)
