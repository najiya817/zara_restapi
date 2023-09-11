from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View,CreateView,UpdateView
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from api.models import *
from .forms import*
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"index.html")
@csrf_exempt
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=RegAdmin.objects.get(username=username,password=password)
            print(user)
            if user is not None:
                # login(request,user)
                return render(request,"home.html")
            else:
                return redirect('logi')
        except:
            return render(request,"log.html")
    return render(request,"log.html")

@csrf_exempt
def reg_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=RegAdmin(username=username,password=password)
        user.save()
        return render(request,"log.html")
    return render(request,"reg.html")

def LandHome(request):
    return render(request,"home.html")

class CategoryView(CreateView):
        model=Category
        form_class=CategoryForm
        template_name="categories.html"
        success_url=reverse_lazy('catg')
        def form_valid(self, form):
            form.instance.user=self.request.user
            self.object=form.save()
            messages.success(self.request,"category added ")
            return super().form_valid(form)
        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            context["data"]=Category.objects.all()
            print(context["data"])
            return context

class EditCategory(UpdateView):
    model=Category
    form_class=CategoryForm
    template_name="editcat.html"
    success_url=reverse_lazy('catg')
    pk_url_kwarg='pk'
    def form_valid(self, form):
        self.object=form.save()
        messages.success(self.request,"category updated succesfully")
        return super().form_valid(form)
    
class BrandView(CreateView):
    model=Brand
    form_class=BrandForm
    template_name="brands.html"
    success_url=reverse_lazy('bnd')
    def form_valid(self, form):
        self.object=form.save()
        messages.success(self.request,"Brand added successfully")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Brand.objects.all()
        print(context["data"])
        return context

class EditBrand(UpdateView):
    model=Brand
    form_class=BrandForm
    template_name="editbrand.html"
    success_url=reverse_lazy('bnd')
    pk_url_kwarg='pk'
    def form_valid(self, form):
        self.object=form.save()
        messages.success(self.request,"brand edited successfully")
        return super().form_valid(form)
