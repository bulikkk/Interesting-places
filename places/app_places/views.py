from django.views import View
from django.shortcuts import render
from django.core import serializers
from .models import Place
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlaceSerializer


class MainView(View):

    def get(self, request):
        p = Place.objects.all()
        qs_json = serializers.serialize('json', p)
        ctx = {'places': qs_json}
        return render(request, 'app_places/index.html', ctx)

    def post(self, request):
        # p = Place.objects.filter(name=)
        pass


class PlacesView(APIView):

    def get(self, request):
        if request.GET.get('text'):
            places = Place.objects.filter(name__icontains=request.GET.get('text')).order_by('name')

        serializer = PlaceSerializer(places, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)