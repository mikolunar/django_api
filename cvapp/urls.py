from django.urls import path

from . import views
from . views import CVView

app_name = 'cvapp'

urlpatterns = [
    path('list', views.CVList.as_view()),
    path('<int:pk>/', views.CVDetail.as_view()),
    path('upload/', CVView.as_view(), name='file-upload'),
    path('get_cv/', views.get_cv, name="getcv"),
    path('hello/', views.say_hello, name="hello"),
    path('', views.home, name="index"),
    path('calendar/', views.printCalendar, name="calendar"),
    path('project', views.project_new, name='project_new')
]

# urlpatterns = [
#     path('', views.PostList.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
# ]
