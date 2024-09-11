from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieHallViewSet,
                          GenreList,
                          ActorList,
                          CinemaHallViewSet)

cinema_halls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

cinema_halls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "delete": "destroy"
})

router = routers.DefaultRouter()
router.register("movies", MovieHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>", GenreList.as_view(), name="genres_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>", ActorList.as_view(), name="actors_detail"),
    path("cinema_halls/", cinema_halls_list, name="cinema_list"),
    path("cinema_halls/<int:pk>", cinema_halls_detail, name="cinema_detail"),
]

app_name = "cinema"
