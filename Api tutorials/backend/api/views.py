from django.shortcuts import render
from . import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getProducts(request):
    product = Products.products
    return Response(product)

@api_view(['GET'])
def getproduct(request,id):
    product = Products.products[id]
    return Response(product)








