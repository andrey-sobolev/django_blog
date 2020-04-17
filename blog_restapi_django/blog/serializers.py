from rest_framework import serializers

from blog.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Like
        fields = [
            'user',
            'post',
        ]

    def __init__(self, *args, **kwargs):
        self.creating = 'data' in kwargs and 'creating' in kwargs['data']
        super().__init__(*args, **kwargs)
        
    def validate(self, data):
        user = data['user']
        post = data['post']
        if self.creating and Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError('This like already exists')
        return data
