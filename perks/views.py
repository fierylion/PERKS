from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['POST'])
def login(request, format=None):
    vendor = get_list_or_404(Vendor, businessName=request.data['businessName'])
    if not vendor.check_password(request.data['password']):
        return Response({"Detail": "not found!."}, status=status.HTTP_404_NOT_FOUND)
    token, created  = Token.objects.get_or_create(vendor=vendor)
    serializedVendor = VendorSerializer(instance=vendor)
    return Response({"token": token.key, "vendor":serializedVendor.data})

@api_view(['POST'])
def signup(request, format=None):
    serializedVendor = VendorSerializer(data=request.data)
    if serializedVendor.is_valid():
        serializedVendor.save()
        vendor = Vendor.objects.get(businessName=request.data['businessName'])
        vendor.set_password(request.data['password'])
        vendor.save()
        token = Token.objects.create(vendor=vendor)
        return Response({"token": token.key, "vendor":serializedVendor.data})
    return Response(serializedVendor.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def vendor_list(request, format=None):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializedVendors = VendorSerializer(vendors, many=True)
        return Response(serializedVendors.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializedVendors = VendorSerializer(data=request.data)
        if serializedVendors.is_valid():
            serializedVendors.save()
            return Response(serializedVendors.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializedUsers = UserSerializer(users, many=True)
        return Response(serializedUsers.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializedUsers = UserSerializer(data=request.data)
        if serializedUsers.is_valid():
            serializedUsers.save()
            return Response(serializedUsers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def transaction_list(request, format=None):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializedTransactions = TransactionSerializer(transactions, many=True)
        return Response(serializedTransactions.data, status=status.HTTP_200_OK) 

    if request.method == 'POST':
        serializedTransactions = TransactionSerializer(data=request.data)
        if serializedTransactions.is_valid():
            serializedTransactions.save()
            return Response(serializedTransactions.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_details(request, id, format=None):
    try:
        vendor = Vendor.objects.get(pk=id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedVendor = VendorSerializer(vendor)
        return Response(serializedVendor.data)
    
    elif request.method == 'PUT':
        serializedVendor = VendorSerializer(vendor, data=request.data)
        if serializedVendor.is_valid():
            serializedVendor.save()
            return Response(serializedVendor.data)
        return Response(serializedVendor.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedUser = UserSerializer(user)
        return Response(serializedUser.data)
    
    elif request.method == 'PUT':
        serializedUser = UserSerializer(user, data=request.data)
        if serializedUser.is_valid():
            serializedUser.save()
            return Response(serializedUser.data)
        return Response(serializedUser.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_details(request, id, format=None):
    try:
        transaction = Transaction.objects.get(pk=id)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedTransaction = TransactionSerializer(transaction)
        return Response(serializedTransaction.data)
    
    elif request.method == 'PUT':
        serializedTransaction = TransactionSerializer(transaction, data=request.data)
        if serializedTransaction.is_valid():
            serializedTransaction.save()
            return Response(serializedTransaction.data)
        return Response(serializedTransaction.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)