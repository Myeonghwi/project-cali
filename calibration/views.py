from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import CaliEnergyForm


# Create your views here.
class ElectricityView(FormView):
    form_class = CaliEnergyForm
    template_name = 'calibration/calibration.html'

    def form_valid(self, form):
        elec_jan = '%d' % self.request.POST['electricity_jan']

        context = {}
        context['form'] = form
        context['elec_jan'] = elec_jan

        return render(self.request, self.template_name, context)

    def form_invalid(self, form):

        pass

