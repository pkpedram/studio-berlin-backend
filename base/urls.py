from django.urls import path
from .views import GeneralSettingRetrieveView, SectionListView, ClientsListView, CounterListView

urlpatterns = [
    path('general-setting/', GeneralSettingRetrieveView.as_view(), name='general-setting'),
    path('sections/', SectionListView.as_view(), name='section-list'),
    path('clients/', ClientsListView.as_view(), name='clients-list'),
    path('counter/', CounterListView.as_view(), name='counter-list'),
    
]