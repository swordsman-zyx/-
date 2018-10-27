from django.shortcuts import render
# Create your views here.

import json
from django.http import HttpResponse
from company.models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from company.forms import CompanyForm
from django.db.models import F
from django.db.models import Q
from django.db.models import Sum

#无参数的方法
@method_decorator(csrf_exempt, name='dispatch')
class CompanyView(View):

    #用form表单接收
    def get(self, request):
        res = CompanyForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        company = Company.objects.filter(company_name=res.data.get('company_name'))
        print(company.values())
        return HttpResponse(status=201)

    #把传入的json信息提取并作为表的数据内容创建新数据
    def post(self, request):
        stream = request.body.decode()
        json_data = json.loads(stream)
        company = Company.objects.create(company_name=json_data['company_name'])
        return HttpResponse(status=201, content={'company_id': company.company_id})

#有参数的方法
@method_decorator(csrf_exempt,name='dispatch')
class CompaniesView(View):

    #带参数的get方法
    def get(self,request,company_name):
        company = Company.objects.get(company_name=company_name)
        print(company.company_id)
        company1 = Company.objects.filter(company_name=company_name)
        print(company1)
        return HttpResponse(status=201)

    def put(self,request,company_id):
        company=Company.objects.get(company_id=company_id)
        Company.objects.get(company_id=company_id).update(company_name='zmy')
        return HttpResponse(status=201)


    def delete(self,request,company_id):
        Company.objects.filter(log_id=company_id).delete()
        return HttpResponse(status=201)


    # def get(self,request,company_id):
    #     try:
    #         company = Company.objects.get(company_name=company_name)
    #     except Compeny.DoesNotExist:
    #         return HttpResponse(company.detail_info())
    #     return HttpResponse(company.detail_info())
