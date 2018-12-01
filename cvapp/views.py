from rest_framework import generics
from . models import CV
from . serializers import CVSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
#
#
from django.http import HttpResponseRedirect


import smtplib
from email.mime.text import MIMEText


def get_cv(request):

    return HttpResponseRedirect('/admin/')


class CVList(generics.ListAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = CVSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
