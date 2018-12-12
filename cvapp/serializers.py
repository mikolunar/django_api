from rest_framework import serializers
from . import models


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CV
        # fields = ('id', 'first_name', 'last_name', 'cv_type', 'cv_lang')
        fields = '__all__'
