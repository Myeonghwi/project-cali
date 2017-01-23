from django import forms


class CaliEnergyForm(forms.Form):
    electricity_jan = forms.FloatField(label='electricity january')
    electricity_feb = forms.FloatField(label='electricity february')
    electricity_mar = forms.FloatField(label='electricity march')
    electricity_apr = forms.FloatField(label='electricity april')
    electricity_may = forms.FloatField(label='electricity may')
    electricity_jun = forms.FloatField(label='electricity june')
    electricity_jul = forms.FloatField(label='electricity july')
    electricity_aug = forms.FloatField(label='electricity august')
    electricity_sep = forms.FloatField(label='electricity september')
    electricity_oct = forms.FloatField(label='electricity october')
    electricity_nov = forms.FloatField(label='electricity november')
    electricity_dec = forms.FloatField(label='electricity december')

    heating_jan = forms.FloatField(label='heating january')
    heating_feb = forms.FloatField(label='heating february')
    heating_mar = forms.FloatField(label='heating march')
    heating_apr = forms.FloatField(label='heating april')
    heating_may = forms.FloatField(label='heating may')
    heating_jun = forms.FloatField(label='heating june')
    heating_jul = forms.FloatField(label='heating july')
    heating_aug = forms.FloatField(label='heating august')
    heating_sep = forms.FloatField(label='heating september')
    heating_oct = forms.FloatField(label='heating october')
    heating_nov = forms.FloatField(label='heating november')
    heating_dec = forms.FloatField(label='heating december')