import json

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MusicalWork
from .serializers import MusicalWorkSerializer


class MusicalWorkList(generics.ListAPIView):
    # API endpoint that allows to view all the MusicalWork stored in db.
    queryset = MusicalWork.objects.all()[:20]
    serializer_class = MusicalWorkSerializer


class MusicalWorkDetail(APIView):
    def get(self, request, format=None):
        return render(request, "search.html", {})

    def post(self, request, format=None):
        iswc = request.data["iswc"]
        musical_work = MusicalWork.objects.filter(iswc=iswc).all()
        musical_work_serializer = MusicalWorkSerializer(musical_work, many=True)
        response = musical_work_serializer.data
        response = json.loads(json.dumps(response))
        return Response(response)
