from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from product.models import Danhmuc, Mon
from cart.models import GioHang, CTGioHang
from customer.models import KhachHang


class Index(View):
    def get(self, request):

        kh = KhachHang.objects.get(maKH= 1)
        giohang= GioHang.objects.get(maKH = kh) # request.user
        count_cart= CTGioHang.objects.filter(maGH=giohang).count()
        print(count_cart)
        
        context={
            'dm': Danhmuc.objects.all(),
            'mon': Mon.objects.filter(trangThaiMon=True),
            'count_cart':count_cart
        }


        return render(request, 'homepage/index.html', context)


def getTopBar(request):

    kh = KhachHang.objects.get(maKH= 1)
    giohang= GioHang.objects.get(maKH = kh) # request.user
    count_cart= CTGioHang.objects.filter(maGH=giohang).count()
    print(count_cart)

    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'count_cart':count_cart
        
    }

    return render(request, 'homepage/topbar.html', context)

