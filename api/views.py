from django.shortcuts import render
from rest_framework import viewsets
from api.models import Checkbox
from api.serializers import CheckBoxSerializer

class CheckboxViewSet(viewsets.ModelViewSet):
    queryset = Checkbox.objects.all()
    serializer_class = CheckBoxSerializer