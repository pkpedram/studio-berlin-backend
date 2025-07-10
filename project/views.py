
# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ProjectCategory, Project
from .serializers import ProjectCategorySerializer, ProjectSerializer, ProjectDetailSerializer

class ProjectCategoryListView(ListAPIView):
    queryset = ProjectCategory.objects.all().order_by('ordering')
    serializer_class = ProjectCategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}

class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by('ordering')
    serializer_class = ProjectSerializer

class ProjectDetailByIDView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}

class ProjectDetailBySlugView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        return {'request': self.request}