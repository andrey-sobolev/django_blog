from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from blog.serializers import PostSerializer, LikeSerializer
from blog.models import Post, Like


class CreatePostView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects


class LikeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    queryset = Like.objects
    
    def post(self, request, *args, **kwargs):
        kwargs['creating'] = True
        serializer = self.get_serializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        instance = self.queryset.filter(**serializer.validated_data).first()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    


