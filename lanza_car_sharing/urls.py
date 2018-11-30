from django.urls import path

from . import views
from . views import CarView

urlpatterns = [
    path('', views.CarList.as_view()),
    path('<int:pk>/', views.CarDetail.as_view()),
    path('upload/', CarView.as_view(), name='file-upload'),

]

# urlpatterns = [
#     path('', views.PostList.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
# ]