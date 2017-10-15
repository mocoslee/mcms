from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class DashBoard(View):

    template_name = "management/dashboard.html"

    def get(self,req):

        return render(req,self.template_name)

