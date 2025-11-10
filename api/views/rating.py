from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Rating
from ..serializers.models_serializers import RatingSerializer


class RatingListCreate(APIView):
    """
    GET → List of all ratings
    POST → Create a new rating
    """

    def get(self, request):
        media_id = request.query_params.get('media_id')
        user_id = request.query_params.get('user_id')
        order_by = request.query_params.get('order_by', '-created_at')

        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        ratings = Rating.objects.all()

        if media_id:
            ratings = ratings.filter(media_id=media_id)
        if user_id:
            ratings = ratings.filter(user_id=user_id)

        ratings = ratings.order_by(order_by)

        total_count = ratings.count()

        if offset:
            try:
                offset = int(offset)
                ratings = ratings[offset:]
            except ValueError:
                return Response({'msg': 'offset must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        if limit:
            try:
                limit = int(limit)
                ratings = ratings[:limit]
            except ValueError:
                return Response({'msg': 'limit must be an integer'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = RatingSerializer(ratings, many=True)

        return Response({
            'count': total_count,
            'limit': limit or total_count,
            'offset': offset or 0,
            'results': serializer.data
        }, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id

        serializer = RatingSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingDetail(APIView):
    """
    GET → Get one Rating
    PUT → Update one Rating
    DELETE → Delete one Rating
    """

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return None

    def get(self, request, pk):
        rating = self.get_object(pk)
        
        if not rating:
            return Response({'error': 'Rating not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RatingSerializer(rating)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        rating = self.get_object(pk)
        
        if not rating:
            return Response({'error': 'Rating not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RatingSerializer(rating, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rating = self.get_object(pk)
        
        if not rating:
            return Response({'error': 'Rating not found'}, status=status.HTTP_404_NOT_FOUND)
        
        rating.delete()
        
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)