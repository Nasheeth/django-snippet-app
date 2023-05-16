from rest_framework import serializers
from .models import Tag, Snippet

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'content', 'timestamp', 'created_user', 'tag']
