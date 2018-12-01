from django.urls import path

from . import views
from . views import CVView

urlpatterns = [
    path('', views.CVList.as_view()),
    path('<int:pk>/', views.CVDetail.as_view()),
    path('upload/', CVView.as_view(), name='file-upload'),

]

# urlpatterns = [
#     path('', views.PostList.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
# ]
