from rest_framework import serializers
from .models import *
from django.conf import settings


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'
