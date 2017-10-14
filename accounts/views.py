from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class AccountView(View):

    template_name = 'accounts/profile.html'

    def get(self, request):
        return render(request, self.template_name)