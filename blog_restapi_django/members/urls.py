from django.urls import path
from members.views import ViewUser

urlpatterns = [
    path('', ViewUser.as_view(), name='hello'),
]
