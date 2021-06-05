from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('post-list/', views.taskList, name="post-list"),
	path('post-detail/<str:pk>/', views.taskDetail, name="post-detail"),
	path('post-create/', views.taskCreate, name="post-create"),

	path('post-update/<str:pk>/', views.taskUpdate, name="post-update"),
	path('post-delete/<str:pk>/', views.taskDelete, name="post-delete"),
]
