from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import DonHang, CTDonHang, KhuyenMai
from cart.models import GioHang, CTGioHang
from customer.models import KhachHang

import datetime
from decimal import Decimal


# Create your views here.

def getDonHang(request):

    today= datetime.date.today()

    kh = KhachHang.objects.get(maKH= 1)
    giohang, created = GioHang.objects.get_or_create(maKH= kh) # request.user
    ct_giohang = CTGioHang.objects.filter(maGH=giohang)

    ship = 30
    total = sum(item.soLuong * item.giaMon for item in ct_giohang) + ship
    print('total1:',    total)

    context={
        'cart_items': ct_giohang,
        'total':total, 
        'ship':ship

    }

    if request.method == 'POST':
        coupon= request.POST.get('coupon')
        # print(coupon)

        if not coupon:
            messages.warning(request,  f"Mã giảm giá không hợp lệ.")
            return redirect('bill')
        
        cp= KhuyenMai.objects.filter(code= coupon, trangThai= True, ngayHetHan__gte = today).values_list('phantramKM', flat=True)
        # cp= KhuyenMai.objects.get(code = coupon, trangThai= True, ngayHetHan__gte = today).phantramKM
        # print(cp)
        # print(sum(cp))

        if cp:
            sotiengiam= round((Decimal(sum(cp)) / 100)*total)
            print('giam:',sotiengiam)
            total_discount = total - sotiengiam +ship
            print('tong:', total_discount)
            context['total_discount']= total_discount
            # KhuyenMai.objects.filter(code= coupon).update(trangThai= False)
            messages.success(request,  f"Sử dụng mã thành công.")
            # return redirect('bill')
        else:
            messages.warning(request,  f"Mã giảm giá không tồn tại hoặc đã hết hạn.")
            return redirect('bill')
   
    # total= total + ship
    # print('total2: ', total)


    return render(request, 'homepage/order/checkout.html', context)
