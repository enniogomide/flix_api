from django.urls import path
from . import views


urlpatterns = [

    path('actors', views.ActorCreateListView.as_view(),
         name='actor_create_list'),
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(),
         name='actor_update_detail_delete'),

]
