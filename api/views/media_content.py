from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import MediaContent
from ..serializers.models_serializers import MediaContentSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample


class MediaContentListCreate(APIView):
    """
    GET → List media content object
    POST → Create new media content object
    """

    def get(self, request):
        category = request.query_params.get('category')
        title = request.query_params.get('title')

        order_by = request.query_params.get('order_by', '-created_at')

        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        media = MediaContent.objects.all()

        if category:
            media = media.filter(category__iexact=category)
        if title:
            media = media.filter(title__icontains=title)

        media = media.order_by(order_by)

        total_count = media.count()

        if offset:
            try:
                offset = int(offset)
                media = media[offset:]
            except ValueError:
                return Response(
                    {'error': 'offset must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if limit:
            try:
                limit = int(limit)
                media = media[:limit]
            except ValueError:
                return Response(
                    {'error': 'limit must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = MediaContentSerializer(media, many=True)

        return Response({
            'count': total_count,
            'limit': limit or total_count,
            'offset': offset or 0,
            'results': serializer.data
        }, status=status.HTTP_200_OK)


    @extend_schema(
        request=MediaContentSerializer,
        responses={201: MediaContentSerializer},
        examples=[
            OpenApiExample(
                'Example',
                description='Example payload',
                value={
                    "title": "Launch Trailer",
                    "description": "New launch trailer for season 2",
                    "category": "video",
                    "thumbnail_url": "http://example.com/thumbS2.png",
                    "content_url": "http://example.com/gameplayS2.mp4"
                },
            ),
        ],
    )
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

    @extend_schema(
        request=MediaContentSerializer,
        responses={
            200: MediaContentSerializer,
            404: OpenApiExample(
                'No encontrado',
                value={'msg': 'Media not found'},
            ),
        },
        examples=[
            OpenApiExample(
                'Update example',
                description='Example to update media information',
                value={
                    "title": "Updated Trailer",
                    "description": "Updated description for the trailer",
                    "category": "video",
                    "thumbnail_url": "http://example.com/newthumb.png",
                    "content_url": "http://example.com/newgameplay.mp4"
                },
            ),
        ],
    )
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
