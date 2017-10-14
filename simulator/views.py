from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class SimulatorView(View):

    template_name = 'simulator/simulator.html'

    def get(self, request):
        return render(request, self.template_name)