from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ReviewSerializer, OrderSerializer, BuyerSerializer, SizeSerializer, CoverSerializer, \
    PatternSerializer, PageSerializer
from .models import Review, Order, Buyer, Cover, Pattern, Size, Page


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order


class BuyerViewset(viewsets.ModelViewSet):
    serializer_class = BuyerSerializer

    def get_queryset(self):
        buyer = Buyer.objects.all()
        return buyer


class CoverViewset(viewsets.ModelViewSet):
    serializer_class = CoverSerializer

    def get_queryset(self):
        cover = Cover.objects.all()
        return cover


class PatternViewset(viewsets.ModelViewSet):
    serializer_class = PatternSerializer

    def get_queryset(self):
        pattern = Pattern.objects.all()
        return pattern


class SizeViewset(viewsets.ModelViewSet):
    serializer_class = SizeSerializer

    def get_queryset(self):
        size = Size.objects.all()
        return size

class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        review = Review.objects.all()
        return review


class PageViewset(viewsets.ModelViewSet):
    serializer_class = PageSerializer

    def get_queryset(self):
        page = Page.objects.all()
        return page
