from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.models import GioHang, CTGioHang
from product.models import Mon, CTGia
from customer.models import KhachHang

from .forms import CtGHForm

# Create your views here.



# @login_required
def add_to_cart(request, mon_id):

    kh = KhachHang.objects.get(maKH= 1)
    giohang, created = GioHang.objects.get_or_create(maKH= kh)  # request.user
    mon = get_object_or_404(Mon, maMon=mon_id)
  
    # soluong = 1

    variant= request.GET.get('variant')
    # print(variant)

    if variant:
        variant= request.GET.get('variant')
        # size= CTGia.objects.get(size=variant)

        price= mon.get_product_price_by_size(mon_id,variant)
        # print(price)
        ct_giohang, created = CTGioHang.objects.get_or_create(maGH=giohang, maMon=mon, giaMon=price, size=variant)
        messages.success(request,  f"{mon.tenMon} đã được thêm vào giỏ hàng.")

        if not created:
            ct_giohang.soLuong += 1
            ct_giohang.save()
            # messages.success(request,  f"{mon.tenMon} đã được thêm vào giỏ hàng.")
            redirect('detailmon',mon_id)
    else:
         messages.warning(request, "Chưa chọn size.")
         return redirect('detailmon',mon_id)

    return redirect('detailmon',mon_id)


def removeCart(request, cart_id):

    CTgiohang= CTGioHang.objects.get(maCTGH= cart_id)
    CTgiohang.delete()
    messages.success(request,  "Xóa thành công.")

    return redirect('cart_view')


def upQuantity(request, cart_id):
    CTgiohang= CTGioHang.objects.get(maCTGH= cart_id)
    CTgiohang.soLuong += 1
    CTgiohang.save()
    messages.success(request,  "Tăng số lượng thành công.")

    return redirect('cart_view')


def downQuantity(request, cart_id):
    CTgiohang= CTGioHang.objects.get(maCTGH= cart_id)
    CTgiohang.soLuong -= 1
    CTgiohang.save()
    messages.success(request,  f"Giảm số lượng thành công.")

    return redirect('cart_view')


# @login_required
def cart_view(request):

    kh = KhachHang.objects.get(maKH= 1)
    giohang, created = GioHang.objects.get_or_create(maKH= kh) # request.user
    ct_giohang = CTGioHang.objects.filter(maGH=giohang)
    total = sum(item.soLuong * item.giaMon for item in ct_giohang)

    context= {
        'cart_items': ct_giohang, 
        'total': total

    }

    return render(request, 'homepage/cart/cart.html', context)

