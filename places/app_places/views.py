from django.views import View
from django.shortcuts import render
from .models import Place


class MainView(View):

    def get(self, request):
        places = Place.objects.all()
        ctx = {'places': places}
        return render(request, 'app_places/main.html', ctx)

