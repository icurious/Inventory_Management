from django.shortcuts import render
from rest_framework import viewsets
from invApp.models import Products,Sales
from invApp.serializer import ProductsSerializer,SalesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from django.http import Http404
# Create your views here.


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class SalesList(APIView):

    def get(self,request):
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            raise Http404


class SalesListInfo(APIView):

    def get_object(self,pk):
        try:
            sale = Sales.objects.get(pk=pk)
            return sale
        except:
            raise Http404
    
    def get(self,request,pk):
        sale = self.get_object(pk)
        serializer = SalesSerializer(sale)
        return Response(serializer.data,status=status.HTTP_200_OK)