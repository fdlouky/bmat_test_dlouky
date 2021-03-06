from rest_framework import serializers

from bmat_app.models import MusicalWork


class MusicalWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicalWork
        fields = ("id", "title", "contributors", "iswc")
