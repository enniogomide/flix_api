from django.urls import path

from . import views

urlpatterns = [

    path('reviews', views.ReviewCreateListView.as_view(), name='review_create_list'),
    path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review_update_detail_delete'),

]
