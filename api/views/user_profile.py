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
        profiles = UserProfile.objects.all().order_by('-created_at')
        serializer = UserProfileSerializer(profiles, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


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