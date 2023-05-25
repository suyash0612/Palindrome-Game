from django.urls import path
from palindrome import views

urlpatterns = [
    path('users/', views.create_user, name='create_user'),
    path('users/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/<int:user_id>/', views.update_user, name='update_user'),
    path('login/', views.user_login, name='user_login'),
    path('users/<int:user_id>/games/', views.create_game, name='create_game'),
    path('games/<str:game_id>/board/', views.get_board, name='get_board'),
    path('games/<str:game_id>/board/', views.update_board, name='update_board'),
    path('games/', views.list_games, name='list_games'),
]