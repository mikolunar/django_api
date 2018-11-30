from django.conf.urls import url, include
from django.contrib import admin
from snippets.resources import NoteResource

from django.conf import settings
from django.conf.urls.static import static


note_resource = NoteResource()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^snippets/', include(note_resource.urls)),
    url(r'^api/', include('lanza_car_sharing.urls')),
      url(r'^api/cars/', include('lanza_car_sharing.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# """testapi01 URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include

# from snippets.resources import NoteResource


# note_resource=NoteResource

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# # ]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^snippets/', include(note_resource.urls)),
# ]
# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)