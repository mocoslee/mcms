from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class BaseShow(View):

    template_name = "layouts/website/wide.html"
    def get(self,req):

        return render(req,self.template_name)
