from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from cs_stats.Permissions import BasePermissions

# Create your views here.

class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = [BasePermissions]

##   @action(detail=False, methods=['get'], url_path='get-important-stats'):
##   def get_important_stats(self, request):
##       stats = Stat.objects.filter(name__in=['total_users', 'total_posts', 'total_comments'])
##       serializer = StatSerializer(stats, many=True)
##       return Response(serializer.data)