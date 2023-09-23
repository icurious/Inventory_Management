from rest_framework import serializers
from invApp.models import Products,Sales

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields= ['product_id','name','price','stock']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields= ['transaction_id', 'product_id','quantity','total_amount']