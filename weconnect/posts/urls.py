from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('new/', views.CreatePost.as_view(), name="create"),
    path('by/<str:username>/', views.UserPosts.as_view(),
         name="for_user"),
    path('<int:pk>/',
         views.PostDetail.as_view(), name="single"),
    path('<int:pk>/delete', views.DeletePost.as_view(), name='delete'),
]
