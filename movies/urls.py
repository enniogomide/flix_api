from django.urls import path
from . import views


urlpatterns = [

    path('movies', views.MovieCreateListView.as_view(), name='movie_create_list'),
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie_update_detail_delete'),
    path('movies/stats', views.MovieStatsView.as_view(), name='movie_stats_views'),

]
