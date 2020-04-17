from rest_framework import generics, mixins, status
from rest_framework.views import Response

from members.models import User
from members.serializers import UserSerializer
from members.tasks import save_clearbit_user_info


class ViewUser(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects
    
    def post(self, request):
        serialized_user = self.get_serializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        
        # we create background task for make quick response  to user
        save_clearbit_user_info.delay(serialized_user.instance.id)
        
        return Response(status=status.HTTP_201_CREATED)
