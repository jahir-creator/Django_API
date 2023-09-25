from typing import Any
from django import http
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from .models import Company
import json

class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args , **kwargs ):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=0):
        if (id > 0):
            users = list(Company.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                datos = {'message': "succes", "user": user}
            else:
                datos = {'message': "User not found..."}
            return JsonResponse(datos)
        else:
            users = list(Company.objects.values())
            if len(users) > 0:
                datos = {'message': "succes", "users": users}
            else:
                datos = {'message': "Users not found..."}
            return JsonResponse(datos)

    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'],age=jd['age'],website=jd['website'])
        datos = {'message': " Saved Succes"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd = json.loads(request.body)
        users = list(Company.objects.filter(id=id).values())
        if len(users) > 0:
            users = Company.objects.get(id=id)
            users.name = jd['name']
            users.age = jd['age']
            users.website = jd['website']
            users.save()
            datos = {'message': "Update Succes"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        users = list(Company.objects.filter(id=id).values())
        if len(users) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message': "Succes removed"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)