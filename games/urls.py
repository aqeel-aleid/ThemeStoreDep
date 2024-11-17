from django.urls import path
from . import views


app_name = "games"

urlpatterns = [
    path("create/", views.create_game_view, name="create_game_view"),
    path("all/", views.view_games, name="all_game_view"),
]