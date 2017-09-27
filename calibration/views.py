import os

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import CaliEnergyForm
from .optimization import cvrmse_optimization


class CaliView(TemplateView):
    template_name = 'calibration/calibration.html'

# Create your views here.
class ElectricityView(FormView):
    form_class = CaliEnergyForm
    template_name = 'calibration/calibration.html'

    year_electricity = []
    list_electricity = ['electricity_jan', 'electricity_feb', 'electricity_mar', 'electricity_apr',
                        'electricity_may', 'electricity_jun', 'electricity_jul', 'electricity_aug',
                        'electricity_sep', 'electricity_oct', 'electricity_nov', 'electricity_dec']

    year_heating = []
    list_heating = ['heating_jan', 'heating_feb', 'heating_mar', 'heating_apr',
                    'heating_may', 'heating_jun', 'heating_jul', 'heating_aug',
                    'heating_sep', 'heating_oct', 'heating_nov', 'heating_dec']

    def form_valid(self, form):

        i = 0
        for elements in self.list_electricity:
            self.year_electricity[i] = float(self.request.POST[elements])
            i += 1

        i = 0
        for elements in self.list_heating:
            self.year_heating[i] = float(self.request.POST[elements])
            i += 1

        context = {}
        context['form'] = form
        context['year_electricity'] = self.year_electricity
        context['year_heating'] = self.year_heating

        cvrmse_optimization(self.year_electricity, self.year_heating)

        return render(self.request, self.template_name, context)

    def form_invalid(self, form):

        pass

