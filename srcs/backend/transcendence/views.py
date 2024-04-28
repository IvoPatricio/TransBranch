from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User as User
from .models import FriendRequest as FriendRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
class UserList(APIView):
    def get(self, request, format=None):
        return Response(13)

class UserDetail(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserCreate(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdate(APIView):
    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(f"User with ID {pk} deleted successfully from DB", status=status.HTTP_200_OK)

class FriendCreate(APIView):
    def post(self, request, getformat=None):

        user1 = request.data.get('user1')
        user2 = request.data.get('user2')
        try:
            FriendsRequestObj = FriendRequest.objects.create(user1_id = user1, user2_id = user2)
            return JsonResponse(FriendsRequestObj.id, safe=False)
        except:
            return JsonResponse("Error", safe=False)


class FriendCancel(APIView):
    def patch(self, request, friend_request_id, format=None):

        try:
            friend_request = FriendRequest.objects.get(pk = friend_request_id)
            friend_request.was_canceled = True
            friend_request.save()
        except:
            return JsonResponse("Error", safe=False)

        return JsonResponse({"Friend request canceled"}, status=status.HTTP_200_OK)

class FriendAccept(APIView):
    def patch(self, request, friend_request_id, format=None):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        friend_request.was_accepted = True
        friend_request.save()
        return JsonResponse({"Friend request accepted"}, status=status.HTTP_200_OK)

class FriendRefuse(APIView):
    def patch(self, request, friend_request_id, format=None):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        friend_request.was_refused = True
        friend_request.save()
        return JsonResponse({"Friend request refused"}, status=status.HTTP_200_OK)

class FriendDetail(APIView):
    def get(self, request, friend_request_id, format=None):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        return JsonResponse({"Friend request details retrieved"})

class UserFriendRequests(APIView):
    def get(self, request, userId, format=None):
        user = get_object_or_404(User, id=userId)
        sent_friend_requests = user.sent_friend_requests.all()
        received_friend_requests = user.received_friend_requests.all()
        return JsonResponse({"sent_friend_requests": sent_friend_requests, "received_friend_requests": received_friend_requests})