from rest_framework import serializers
from app1_manager.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('Title', 'Image', 'User')
