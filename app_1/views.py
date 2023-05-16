from rest_framework import generics, permissions, status
from .models import Tag, Snippet
from .serializers import TagSerializer, SnippetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class SnippetOverviewAPI(generics.ListAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class SnippetCreateAPI(generics.CreateAPIView):
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

class SnippetDetailAPI(generics.RetrieveAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class SnippetUpdateAPI(generics.UpdateAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class SnippetDeleteAPI(generics.DestroyAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TagListAPI(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TagDetailAPI(generics.RetrieveAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class SnippetCreateAPI(APIView):
    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            tag_title = serializer.validated_data.get('tag_title')
            tag = get_object_or_404(Tag, title=tag_title)
            if not tag:
                tag = Tag.objects.create(title=tag_title)
            serializer.validated_data['tag_id'] = tag.id
            snippet = Snippet.objects.create(**serializer.validated_data)
            response_data = {
                'snippet_id': snippet.id,
                'title': snippet.title,
                'content': snippet.content,
                'timestamp': snippet.timestamp,
                'tag_id': snippet.tag_id
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
