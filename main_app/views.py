from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Finch, Car, Body

from django.views.generic.edit import CreateView 
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bodys"] = Body.objects.all()
        return context



class About(TemplateView):
   template_name = 'about.html'


class FinchList(TemplateView):
    template_name = 'finch_list.html'

    def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            name = self.request.GET.get('name')
            if name != None:
                context['finches'] = Finch.objects.filter(name__icontains=name)
                context['header'] = f'searching for {name}'
            else:
                context['finches'] = Finch.objects.all()
                context['header'] = 'Finch Collection'

            return context
class FinchCreate(CreateView):
    model = Finch
    fields = ['name','img', 'info']
    template_name = 'finch_create.html'
    success_url = '/finches/'

class FinchDetail(DetailView):
    model = Finch
    template_name = 'finch_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bodys"] = Body.objects.all()
        return context


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name','img', 'info']
    template_name = 'finch_update.html'
    success_url = '/finches/'

class FinchDelete(DeleteView):
    model = Finch
    template_name = 'finch_delete_confirmation.html'
    success_url = '/finches/'

class CarCreate(View):
    def post(self, request, pk):
        make = request.POST.get("make")
        model = request.POST.get("model")
        finch = Finch.objects.get(pk=pk)
        Car.objects.create(make=make, model=model, finch=finch)
        return redirect('finch_detail', pk=pk)

class BodyCarAssoc(View):

    def get(self, request, pk, car_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Body.objects.get(pk=pk).cars.remove(car_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Body.objects.get(pk=pk).cars.add(car_pk)
        return redirect('home')

