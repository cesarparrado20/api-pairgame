from django.db import models


class World(models.Model):
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "world"
        verbose_name_plural = "worlds"
        db_table = "worlds"

    def __str__(self):
        return "World {}".format(self.id)


class Image(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    publication_date = models.DateField()
    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        db_table = "images"

    def __str__(self):
        return "Image: {}".format(self.id)
