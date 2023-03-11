from django.shortcuts import render,redirect
from django.contrib import messages

from order.models import DonHang, CTDonHang

# Create your views here.


def getViewCustomer(request):
    return render(request, "homepage/customer/customer.html")


def index(request):

    dhOfKh = DonHang.objects.filter(maKH = 1)


    context = {
        'listdh' : dhOfKh,
    }
    return render(request, 'homepage/customer/customer.html', context)


def cancel_dh(request, int):

    if DonHang.objects.filter(maDH = int).exists():

        dh_cancel = DonHang.objects.get(maDH = int)
        print(dh_cancel)
        dh_cancel.delete()
        messages.success(request,  f"Xóa đơn hàng thành công.")


    return redirect('index')
