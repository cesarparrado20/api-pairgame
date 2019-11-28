from rest_framework import serializers

from worlds.models import World, Image


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ["id", "description"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "description", "url", "publication_date"]
