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
        # giohang= GioHang.objects.get(maKH = kh, trangThai= True) # request.user
        # if giohang:
        #     count_cart= CTGioHang.objects.filter(maGH=giohang).count()
        # print(count_cart)
        
        
        context={
            'dm': Danhmuc.objects.all(),
            'mon': Mon.objects.filter(trangThaiMon=True)
            
        }


        return render(request, 'homepage/index.html', context)


def getTopBar(request):

    kh = KhachHang.objects.get(maKH= 1)
    giohang= GioHang.objects.get(maKH = kh, trangThai= True) # request.user
    if giohang:
        count_cart= CTGioHang.objects.filter(maGH=giohang).count()
    print(count_cart)

    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'count_cart':count_cart
        
    }

    return render(request, 'homepage/topbar.html', context)


def search(request):
    url = request.META.get('HTTP_REFERER');

    key = request.GET.get("value_search");
    if key is None:
        return redirect(Index(View))

    kh = KhachHang.objects.get(maKH=1)
    giohang = GioHang.objects.get(maKH=1, trangThai= True)  # request.user
    if giohang:
        count_cart = CTGioHang.objects.filter(maGH=giohang).count()

    result = Mon.objects.filter(tenMon__search = key)

    print(result)

    context = {
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'montk': result,    #  Mon.objects.filter(trangThaiMon=True),
        'count_cart': count_cart
    }

    return render(request, 'homepage/index.html', context)

