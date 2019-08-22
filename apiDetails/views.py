

from django.contrib.admin.views import autocomplete
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bankings_info
from django.http import JsonResponse
from django.db.models import Q

from .serializer import bankSerializer
# Create your views here.


class BranchAutocomplete(APIView):
    def get(self,request):
        query= request.GET.get('q')
        query.upper()
        limit=request.GET.get('limit')
        limit=int(limit)
        offset = request.GET.get('offset')

        bank_data = Bankings_info.objects.all()
        lookup = (Q(branch__istartswith=query.upper()) and Q(branch__contains=query.upper()))
        bank_data=bank_data.filter(lookup).distinct().order_by("ifsc")[int(offset):int(limit) + 1]
        serializer=bankSerializer(bank_data,many=True)
        if(serializer.data == ""):
            return Response(get_object_or_404())
        else:
            return Response(serializer.data)


class Branches(APIView):
    def get(self,request):
        query = request.GET.get('q')
        limit = request.GET.get('limit')
        offset = request.GET.get('offset')
        branch_data=Bankings_info.objects.all()
        lookup= (Q(city__iexact=query.upper())|Q(address__contains=query.upper())|Q(branch__contains=query.upper())|Q(district__contains=query.upper()))
        branch_data=branch_data.filter(lookup).distinct().order_by("ifsc")[int(offset):int(limit)]
        serialse=bankSerializer(branch_data,many=True)
        return Response(serializer.data)


