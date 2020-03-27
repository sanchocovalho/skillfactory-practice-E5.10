from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.template import loader, RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Car
from app.forms import CarForm

def error_404_view(request, exception):
    return render(request, '404.html')

class CarDelete(LoginRequiredMixin, DeleteView):
    login_url = '/'
    redirect_field_name = ''
    model = Car
    success_url = reverse_lazy('app:car-list')
    template_name = 'car_delete.html'

class CarUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = ''
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('app:car-list')
    template_name = 'car_edit.html'

class CarCreate(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = ''
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('app:car-list')
    template_name = 'car_edit.html'

class CarList(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self):
        if 'btnSearch' in self.request.GET:
            query = self.request.GET.get('search', '')
            flag = False
            if query == 'механика' or query == 'Mеханика' \
                or query == 'МЕХАНИКА':
                query = 1
                flag = True
            elif query == 'автомат' or query == 'Автомат' \
                or query == 'АВТОМАТ':
                query = 2
                flag = True
            elif query == 'робот' or query == 'Робот' \
                or query == 'РОБОТ':
                query = 3
                flag = True
            if flag:
                car_list = Car.objects.filter(
                    gearbox=query)
            else:
                car_list = Car.objects.filter(
                    Q(manufacturer__icontains=query)|
                    Q(model__icontains=query)|
                    Q(release_year__icontains=query)|
                    Q(color__icontains=query))
            return car_list
        return Car.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if 'btnLogIn' in request.POST:
            template = loader.get_template('car_list.html')
            cars = Car.objects.all()
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                msg_data = {"errmsg": 0,
                            "object_list": cars,}
            else:
                msg_data = {"errmsg": 1,
                            "object_list": cars,}
            return HttpResponse(template.render(msg_data, request)) 
            # return redirect('/')
        elif 'btnLogOut' in request.POST:
            logout(self.request)
            return redirect('/')
        elif 'btnAddAuto' in request.POST:
            return redirect('/create/')
        return super(CarList, self).dispatch(request, *args, **kwargs)

