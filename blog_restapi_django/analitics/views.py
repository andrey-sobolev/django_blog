from django.db.models import Count, Sum
from django.http import JsonResponse

from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from analitics.serializers import AnaliticSerializer
from blog.models import Post, Like


class GetLikeAnalitic(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        serializer = AnaliticSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        result = self._get_stat(serializer.validated_data)
        return Response(result)
    
    @staticmethod
    def _get_stat(data):
        result = {}
        for user, date_, count in Like.objects.\
                filter(date__date__gte=data['date_from'], date__date__lte=data['date_to']).\
                values_list('user__email', 'date__date'). \
                annotate(count=Count('id')).order_by('-date__date'):
            date_ = date_.isoformat()
            result.setdefault(date_, {})
            result[date_].setdefault(user, 0)
            result[date_][user] += count
        return result

