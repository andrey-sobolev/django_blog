from django.urls import path
from blog.views import CreatePostView, LikeView

urlpatterns = [
    path('', CreatePostView.as_view(), name='create_post'),
    path('<int:post>/like/', LikeView.as_view(), name='like'),
]
