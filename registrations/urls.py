from django.urls import path
from .views import TargetCrateView

urlpatterns = [
    path('registration/target/', TargetCrateView.as_view(), name='reg-target'),

]
