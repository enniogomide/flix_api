from django.urls import path
from . import views


urlpatterns = [

    path('genres', views.GenreCreateListView.as_view(), name='genre_create_list'),
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre_update_detail_delete'),

]
