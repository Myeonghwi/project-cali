from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
# Home View
class HomeView(TemplateView):
    template_name = 'index/index.html'


# User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
