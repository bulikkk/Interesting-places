from django.views import View
from django.shortcuts import render
import json
from django.core import serializers
from .models import Place


class MainView(View):

    def get(self, request):
        p = Place.objects.all()
        qs_json = serializers.serialize('json', p)
        ctx = {'places': qs_json}
        return render(request, 'app_places/main.html', ctx)

    def post(self, request):
        # stworzenie formularza!
        pass
