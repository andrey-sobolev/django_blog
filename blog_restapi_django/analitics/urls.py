from django.urls import path
from analitics.views import GetLikeAnalitic

urlpatterns = [
    path('', GetLikeAnalitic.as_view(), name='like_analitic'),
]
