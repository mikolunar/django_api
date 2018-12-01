from rest_framework import serializers
from . import models


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'cv_type', 'cv_lang')
        model = models.CV
