from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .serializers.serializers_friendrequest import FriendRequestSerializer
from .models import User as User
from .models import FriendRequest as FriendRequest

#POST sends data to the server. 
class FriendCreate(APIView):
    def post(self, request, format=None):
        user1 = request.data.get('user1')
        user2 = request.data.get('user2')
        try:
            friend_request = FriendRequest.objects.create(user1_id=user1, user2_id=user2)
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return JsonResponse({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#PATCH updates resources on the server. 
class FriendCancel(APIView):
    def patch(self, request, friend_request_id, format=None):

        try:
            friend_request = FriendRequest.objects.get(pk = friend_request_id)
            friend_request.was_canceled = True
            friend_request.save()
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return JsonResponse({'Error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FriendAccept(APIView):
    def patch(self, request, friend_request_id, format=None):
        try:
            friend_request = FriendRequest.objects.get(pk = friend_request_id)
            friend_request.was_accepted = True
            friend_request.save()
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return JsonResponse({'Error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FriendRefuse(APIView):
    def patch(self, request, friend_request_id, format=None):
        try:
            friend_request = FriendRequest.objects.get(pk = friend_request_id)
            friend_request.was_refused = True
            friend_request.save()
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return JsonResponse({'Error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#GET retrieves data from the server
class FriendDetail(APIView):
    def get(self, request, friend_request_id, format=None):
        try:
            friend_request = FriendRequest.objects.get(pk = friend_request_id)
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return JsonResponse({'Error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#class UserFriendRequests(APIView):
#    def get(self, request, userId, format=None):
#        try:
#            user = user.objects.get(pk = userId)
#            user.
#        except Exception as error:
#            return JsonResponse({'Error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)