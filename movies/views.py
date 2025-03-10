from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieStatsSerializer, MovieListDetailedSerializer
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailedSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailedSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(total_movies_by_genre=Count('id')).order_by('genre__name')
        total_reviews = Review.objects.count()
        total_reviews_by_movie = Review.objects.values('movie__title').annotate(total_reviews_by_movie=Count('id')).order_by('movie__title')
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        #
        # não precisa ser serializar neste caso.
        #
        # return response.Response(
        #     data = {
        #         'total_movies': total_movies,
        #         'movies_by_genre': movies_by_genre,
        #         'total_reviews': total_reviews,
        #         'total_reviews_by_movie': total_reviews_by_movie,
        #         'average_stars': round(average_stars, 1) if average_stars else 0,
        #     },
        #     status = status.HTTP_200_OK,
        # )

        # usando o serializer
        movies_stats = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'total_reviews_by_movie': total_reviews_by_movie,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }
        serializer = MovieStatsSerializer(data=movies_stats)
        serializer.is_valid(raise_exception=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
