# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response 
from rest_framework import status
from  rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_204_NO_CONTENT
)



"""
APIVIEWS (get , post , put , patch , delete)
class ProductApiView(APIView):
#get specific product 
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
            if product:
                print('ooo')
                serializer = ProductSerializer(product)
                return Response(serializer.data , status= HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error':'product not found'},status=HTTP_404_NOT_FOUND)
        
#create specific product         
    def post(self,request):
        serializer = ProductSerializer(data = request.data )
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response({'message':'product successfully created '},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk):
        try:
            product = Product.objects.get(pk = pk)
            serializer = ProductSerializer(product , data = request.data )
            serializer.is_valid(raise_exception = True)
            post = serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        except:
            return Response({'msg':'product not found'},status = status.HTTP_400_BAD_REQUEST)
    
        # instance = self.get_object()
        # serializer = self.get_serialzier(instance,data=request.data )
        # serializer.is_valid(raise_exception = True)
        # instance = serializer.save()
    
    def patch(self , request ,pk):
        try:
            product = Product.objects.get(pk = pk)
            serializer = ProductSerializer(product,data = request.data , partial = True)
            serializer.is_valid(raise_exception = True)
            product = serializer.save()
            print('product',product)
            print('serializer',serializer)  #serializer ProductSerializer(<Product: product 6666>, data={'name': 'product 6666', 'description': 'just product 5', 'price': 3200}, partial=True):
                                            # id = IntegerField(label='ID', read_only=True)
                                            # name = CharField(max_length=100)
                                            # description = CharField(style={'base_template': 'textarea.html'})
                                            # price = DecimalField(decimal_places=2, max_digits=10)
    
            print('serializer data :',serializer.data)  #serializer data : {'id': 4, 'name': 'product 6666', 'description': 'just product 5', 'price': '3200.00'}
            return Response(serializer.data , status = status.HTTP_200_OK)
        except : 
            return Response({'msg':'product not found'},status = status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self,request,pk): 
        product = Product.objects.get(pk = pk)
        product.delete()
        return Response({'msg':'product deleted'},status = status.HTTP_204_NO_CONTENT)
   
    """

    

"""
#MODELVIEWSETS
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self,request):
        serializer = ProductSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        try:
            # product = self.get_object()
            product = Product.objects.get(pk = pk)
            serializer = self.get_serializer(product)
            #Note : no use of is valid in retrieve
            # serializer.is_valid(raise_exception = True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'err':'product not found'},status = status.HTTP_400_BAD_REQUEST)

    
    def update(self,request,pk=None):
        try:
            product = self.get_object()
            serializer = self.get_serializer(product,data= request.data)
            serializer.is_valid(raise_exception = True)
            return Response(serializer.data , status= status. HTTP_200_OK)
            
        except Product.DoesNotExist:
            return Response({'err':'product not found'})
    
    def partial_update(self,request,pk = None):
        try:
            product = self.get_object()
            serializer = ProductSerializer(product,data=request.data,partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'err':'product not found'},status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request, pk =None):
        product = self.get_object()
        if product:
           product.delete()
        return Response({'err':'product deleted'},status = status.HTTP_204_NO_CONTENT)

"""


# @api_view(['GET'])
# def get_product(request,pk):
#     product = Product.get_object_or_404(Product,pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data ,status = status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    # product = Product.objects.get(pk = pk)
    serializer =  ProductSerializer(product)
    return Response(serializer.data , status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset,many = True)
    return Response(serializer.data , status=status.HTTP_200_OK)



    
        
                
     
    
        

            


