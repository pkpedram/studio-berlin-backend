from django.urls import path
from .views import ProjectCategoryListView, ProjectDetailByIDView, ProjectListView, ProjectDetailBySlugView

urlpatterns = [
    path('categories/', ProjectCategoryListView.as_view(), name='project-category-list'),
    path('', ProjectListView.as_view(), name='project-list'),
    path('id/<int:id>/', ProjectDetailByIDView.as_view(), name='project-detail-id'),
    path('slug/<slug:slug>/', ProjectDetailBySlugView.as_view(), name='project-detail-slug'),
]