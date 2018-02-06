from django.urls import path
from . import views


urlpatterns = [
    path('', views.webtoon_list, name="webtoon_list"),
    path('<int:webtoon_id>/', views.webtoon_detail, name="webtoon_detail")
]