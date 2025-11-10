from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class Test(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'API working'}, status=status.HTTP_200_OK)

class TestAuthentication(APIView):
    def get(self, request):
        return Response({'API authentication working'}, status=status.HTTP_200_OK)