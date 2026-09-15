from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.api.serializers import PostSerializer
from posts.models import Post


class PostApiView(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
