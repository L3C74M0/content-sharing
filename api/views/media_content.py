from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import MediaContent
from ..serializers.models_serializers import MediaContentSerializer


class MediaContentListCreate(APIView):
    """
    GET → List media content object
    POST → Create new media content object
    """

    def get(self, request):
        media = MediaContent.objects.all().order_by('-created_at')
        serializer = MediaContentSerializer(media, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = MediaContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaContentDetail(APIView):
    """
    GET → Get one specific media content object
    PUT → Update one media content object
    DELETE → Delete one media content object
    """

    def get_object(self, pk):
        try:
            return MediaContent.objects.get(pk=pk)
        except MediaContent.DoesNotExist:
            return None


    def get(self, request, pk):
        media = self.get_object(pk)
        
        if not media:
            return Response({'msg': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MediaContentSerializer(media)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        media = self.get_object(pk)
        
        if not media:
            return Response({'msg': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MediaContentSerializer(media, data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        media = self.get_object(pk)
        
        if not media:
            return Response({'msg': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)
        
        media.delete()
        
        return Response({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
