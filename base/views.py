
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import GeneralSetting, Section, Clients, CounterItem
from .serializers import GeneralSettingSerializer, SectionSerializer, ClientSerializer, CounterSerializer

class GeneralSettingRetrieveView(APIView):
    def get(self, request):
        try:
            settings = GeneralSetting.objects.first()
            if settings:
                serializer = GeneralSettingSerializer(settings)
                return Response(serializer.data)
            return Response({"detail": "No general settings found."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)



class SectionListView(ListAPIView):
    queryset = Section.objects.all().order_by('ordering')
    serializer_class = SectionSerializer

class ClientsListView(ListAPIView):
    queryset = Clients.objects.all().order_by('ordering')
    serializer_class = ClientSerializer

class CounterListView(ListAPIView):
    queryset = CounterItem.objects.all().order_by('ordering')
    serializer_class = CounterSerializer