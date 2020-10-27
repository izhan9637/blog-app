from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
	path('<int:pk>/', PostDetailView.as_view(), name="detailcreate"),
	path('', PostList.as_view(), name="listcreate")
]
