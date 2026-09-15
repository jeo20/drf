from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


"""
class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        serializer = PostSerializer(Post.objects.filter(pk=pk), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
"""
