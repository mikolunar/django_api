from django.conf.urls import url, include
from django.contrib import admin
from snippets.resources import NoteResource

from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from posts import views as post_views
from django.contrib.auth import views as auth_views

note_resource = NoteResource()
urlpatterns = [
    url(r'', include('cvapp.urls'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^snippets/', include(note_resource.urls)),
    url(r'^api/cv/', include('cvapp.urls')),
    url(r'^api/cars/', include('lanza_car_sharing.urls')),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^posts/', post_views.post, name='post'),


    # url(r'/cv', include('cvapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


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
