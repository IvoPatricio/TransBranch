from django.urls import path
from . import views
from django.urls import path
from .views import UserCreate, UserList, UserDetail, UserUpdate, UserDelete
from .views import FriendCreate, FriendCancel, FriendAccept, FriendRefuse, FriendDetail, UserFriendRequests

urlpatterns = [
    path('create_user/', UserCreate.as_view(), name='create_user'),
	path('users/', views.UserList.as_view(), name='users'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
	path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
	path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),

	path('friend_requests', views.FriendCreate.as_view(), name='Friend_Create'),
    path('friend_requests/<int:friendRequestId>/cancel', views.FriendCancel.as_view(), name='friend_cancel'),
    path('friend_requests/<int:friendRequestId>/accept', views.FriendAccept.as_view(), name='friend_accept'),
    path('friend_requests/<int:friendRequestId>/refuse', views.FriendRefuse.as_view(), name='friend_refuse'),
    path('friend_requests/<int:friendRequestId>', views.FriendDetail.as_view(), name='friend_detail'),
    path('users/<int:userId>/friend_requests', views.UserFriendRequests.as_view(), name='user_friend_requests'),
]