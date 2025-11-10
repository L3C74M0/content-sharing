from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import UserProfile
from ..serializers.models_serializers import UserProfileSerializer


class UserProfileList(APIView):
    """
    GET → List all users profiles
    """

    def get(self, request):
        user_id = request.query_params.get('user_id')
        username = request.query_params.get('username')

        order_by = request.query_params.get('order_by', '-created_at')

        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        profiles = UserProfile.objects.select_related('user').all()

        if user_id:
            profiles = profiles.filter(user_id=user_id)
        if username:
            profiles = profiles.filter(user__username__icontains=username)

        profiles = profiles.order_by(order_by)

        total_count = profiles.count()

        if offset:
            try:
                offset = int(offset)
                profiles = profiles[offset:]
            except ValueError:
                return Response(
                    {'error': 'offset must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if limit:
            try:
                limit = int(limit)
                profiles = profiles[:limit]
            except ValueError:
                return Response(
                    {'error': 'limit must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = UserProfileSerializer(profiles, many=True)

        return Response({
            'count': total_count,
            'limit': limit or total_count,
            'offset': offset or 0,
            'results': serializer.data
        }, status=status.HTTP_200_OK)


class UserProfileDetail(APIView):
    """
    GET → Get one profile
    PUT → Update one profile
    DELETE → Delete one profile
    """

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return None

    def get(self, request, pk):
        profile = self.get_object(pk)
        
        if not profile:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserProfileSerializer(profile)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        profile = self.get_object(pk)
        
        if not profile:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        profile = self.get_object(pk)
        
        if not profile:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        profile.delete()
        
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)