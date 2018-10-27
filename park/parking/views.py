from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from parking.models import Parking
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from company.models import Company
from parking.forms import ParkingForm
import json

#无参数的get,post方法
@method_decorator(csrf_exempt,name='dispatch')
class ParkingView1(View):
    #get方法从FORM表单中接受数据并验证
    def get(self,request):
        res = ParkingForm(request.GET)
        if not res.is_valid():
            return HttpResponse(status=422)
        print(res.data)
        return HttpResponse(status=201)

    #post方法从FORM表单中接收数据并验证
    def post(self,request):
        res = ParkingForm(request.POST)
        if not res.is_valid():
            return HttpResponse(status=422)
        Parking.objects.create(parking_name='meixing_parking')
        return HttpResponse(status=201)

    #在Postman中用json格式向新建的数据中传递值
    def post(self,request):
        stream = request.body.decode()
        json_data = json.loads(stream)
        # print(type(json_data))
        Parking.objects.create(parking_name=json_data['parking_name'])
        return HttpResponse(status=201)

#可以传递参数的方法
@method_decorator(csrf_exempt,name='dispatch')
class ParkingView2(View):

    #根据传入的parking_name获得parking的各个属性信息信息以及全部信息
    # def get(self,request,parking_name):
    #     data=Parking.objects.get(parking_name=parking_name)
    #     data1=Parking.objects.filter(parking_name=parking_name)
    #     print(data1.values_list())
    #     return HttpResponse(status=201)

    #给停车场的名字,找出对应公司的所有信息
    def get(self,request,parking_name):
        parking = Parking.objects.get(parking_name=parking_name)
        company = Company.objects.filter(company_id=parking.company_id)
        print(company.values_list())
        return HttpResponse(status=201)

    #给公司和停车场的名字把两个表的外键连在一起
    def put(self,request,company_name,parking_name):
        company=Company.objects.filter(company_name=company_name)
        uuid11=company.values_list()[0][0]
        Parking.objects.filter(parking_name=parking_name).update(company_id=uuid11)
        return HttpResponse(status=201)

    #根据停车场名字删除停车场信息
    def delete(self,request,parking_name):
        Parking.objects.get(parking_name=parking_name).delete()
        return HttpResponse(status=201)