from django.urls import path
from .views import TargetCrateView, TargetList

urlpatterns = [
    path('registration/target/', TargetCrateView.as_view(), name='reg-target'),
    path('targets/', TargetList.as_view(), name='targets'),

]
