from django.views.generic import View
from .process import html_to_pdf
from .models import invoices
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.
class Generatepdf(View):
    def get(self,request,*args,**kwargs):
        data=invoices.objects.get(id=2)
        open('temp.html','w').write(render_to_string('result.html',{'data':data}))
        pdf=html_to_pdf('result.html')
        return HttpResponse(pdf,content_type='application/pdf')