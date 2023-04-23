from rest_framework.routers import DefaultRouter
from django.urls import include, path

from cats.views import CatViewSet

router = DefaultRouter()

router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls))
]




# С дженериками Джанго
# from django.urls import include, path

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]


# c вьюклассами Джанго
# from django.urls import include, path

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]