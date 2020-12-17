from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Target


class TargetCrateView(CreateView):
    model = Target
    fields = ['name', 'latitude', 'longitude', 'exp_date']
    template_name = '../registrations/templates/registrations/targets/target.html'
    success_message = 'Target Successfully created'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        return super().form_invalid(form)
