import os

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import CaliEnergyForm
from .optimization import cvrmse_optimization


# Create your views here.
class CalibrationView(TemplateView):
    template_name = 'calibration/calibration.html'

    def post(self, request, *args, **kwargs):

        elec_list = []
        gas_list = []

        for i in range(1, 12):
            elec_code = f'elec_{i}'
            gas_code = f'gas_{i}'
            elec_list.append(request.POST[elec_code])
            gas_list.append(request.POST[gas_code])
            
        rate_dict = {
            'start_at': request.POST['start_at'],
            'period': request.POST['period'],
            'interest_rate': request.POST['interest_rate'],
            'elec_rate': request.POST['elec_rate'],
            'gas_rate': request.POST['gas_rate'],
            'green_rate': request.POST['green_rate']
        }

        self.auto_calc_rate(rate_dict)

        return render(request, self.template_name)


    def auto_calc_rate(self, rate_dict):
        pass

