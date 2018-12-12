from django.shortcuts import render
from django.core.serializers import serialize
import json

from rest_framework import generics
from . models import CV
from . forms import ProjectForm
from . serializers import CVSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

import smtplib
from email.mime.text import MIMEText

import calendar


cv_schema = {

    "basics": {
        "name": "John Doe",
        "label": "Programmer",
        "picture": "",
        "email": "john@gmail.com",
        "phone": "(912) 555-4321",
        "website": "http://johndoe.com",
        "summary": "A summary of John Doe...",
        "location": {
            "address": "2712 Broadway St",
            "postalCode": "CA 94115",
            "city": "San Francisco",
            "countryCode": "US",
            "region": "California"
        },
        "profiles": [{
            "network": "Twitter",
            "username": "john",
            "url": "http://twitter.com/john"
        }]
    },
    "work": [{
        "company": "Company",
        "position": "President",
        "website": "http://company.com",
        "startDate": "2013-01-01",
        "endDate": "2014-01-01",
        "summary": "Description...",
        "highlights": [
            "Started the company"
        ]
    }],
    "volunteer": [{
        "organization": "Organization",
        "position": "Volunteer",
        "website": "http://organization.com/",
        "startDate": "2012-01-01",
        "endDate": "2013-01-01",
        "summary": "Description...",
        "highlights": [
            "Awarded 'Volunteer of the Month'"
        ]
    }],
    "education": [{
        "institution": "University",
        "area": "Software Development",
        "studyType": "Bachelor",
        "startDate": "2011-01-01",
        "endDate": "2013-01-01",
        "gpa": "4.0",
        "courses": [
            "DB1101 - Basic SQL"
        ]
    }],
    "awards": [{
        "title": "Award",
        "date": "2014-11-01",
        "awarder": "Company",
        "summary": "There is no spoon."
    }],
    "publications": [{
        "name": "Publication",
        "publisher": "Company",
        "releaseDate": "2014-10-01",
        "website": "http://publication.com",
        "summary": "Description..."
    }],
    "skills": [{
        "name": "Web Development",
        "level": "Master",
        "keywords": [
            "HTML",
            "CSS",
            "Javascript"
        ]
    }],
    "languages": [{
        "language": "English",
        "fluency": "Native speaker"
    }],
    "interests": [{
        "name": "Wildlife",
        "keywords": [
            "Ferrets",
            "Unicorns"
        ]
    }],
    "references": [{
        "name": "Jane Doe",
        "reference": "Reference..."
    }]

}


def home(request):

    context = {
        # 'resume': cv_schema,
        'resume': json.loads(serialize('json', CV.objects.all())),
        'title': 'CV APP Home Page'
    }
    return render(request, 'cvapp/home.html', context)


def get_cv(request):
    cv1 = get_object_or_404(CV, pk=4)
    data = {"first_name": cv1.first_name, "last_name": cv1.last_name}
    return JsonResponse(data)


def printCalendar(request):
    return HttpResponse(calendar.TextCalendar().formatyear(2018))


def say_hello(request):
    return JsonResponse({"response": "Hello this is CV App"})


def project_new(request):
    form = ProjectForm()
    return render(request, 'cvapp/projects.html', {'form': form})


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
