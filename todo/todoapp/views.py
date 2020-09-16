from django.shortcuts import render,reverse
from django.http import HttpRequest,HttpResponseRedirect
from django.views.generic import ListView,CreateView,TemplateView
from . import models
from django.utils.timezone import datetime
import datetime
from bootstrap_datepicker_plus import DateTimePickerInput
# Create your views here.

class TemplateViewTask(TemplateView):
    template_name = 'todoapp/Task_list.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class TaskListView(ListView):
    model = models.Task
    context_object_name = 'task_list'
    template_name = 'todoapp/Task_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.date
        context["present_date"] = now
        return context
    
    def get_queryset(self):
        today = datetime.date.today()
        return models.Task.objects.filter(target_date__year=today.year, target_date__month=today.month, target_date__day=today.day)

class TaskCreateView(CreateView):
    model = models.Task
    template_name = 'todoapp/task_form.html'
    fields = ('name','detail','target_date')

    def get_form(self):
        form = super(TaskCreateView,self).get_form()
        form.fields['target_date'].widget = DateTimePickerInput()
        return form
    
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

        
    
    
    

    

