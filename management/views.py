from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class DashBoard(View):

    template_name = "management/dashboard.html"

    def get(self,req):

        return render(req,self.template_name)


class TestC(View):

    def get(self,req):
        return HttpResponse("hello")
