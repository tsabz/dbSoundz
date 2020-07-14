from rest_framework import serializers
from dbsoundz_data.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('artist_name', 'artist_genre', 'artist_notes')
