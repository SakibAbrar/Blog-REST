from django.urls import path, include
from . import views

app_name = 'post'


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostRetrieveDestroy.as_view()),
    path('<int:pk>/vote', views.VoteCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]