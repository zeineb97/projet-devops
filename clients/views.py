from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from clients.models import Client
from clients.serializers import ClientSerializer
from django.views import View


class UserViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class docView(View): 
    def get(self, request):
        return render(request,'docs/_build/html/index.html')