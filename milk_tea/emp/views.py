from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# from qly_dh.models import DonHang
from django.contrib import messages

from order.models import DonHang

# Create your views here.

def index(request):
    # list = DonHang.objects.exclude(trangThaiDH = '5')
    list = DonHang.objects.all()


    context = {
        'list' : list,
    }

    return render(request, "homepage/base/sidebar.html", context)


def view(request):
    list_all = DonHang.objects.all()
    # print("list: ",list_all)

    context = {
        'list_donhang' : list_all,
    }

    for item in list_all:
        item.ngayLap = item.ngayLap.strftime('%Y/%m/%d, %H:%M:%S')
        item.tongTien = '{:,}'.format(item.tongTien)
        


    return render(request, "homepage/base/tables_handle_dh.html", context)

# ==================================
# xử lý trạng thái đơn hàng
# ===================================


def delete_dh(request, input_id):  # 1 xóa đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '0'
        dh.save()
        return HttpResponseRedirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def accept_dh(request, input_id):   # 2 xác nhận đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '2'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def process_dh(request, input_id):  # 3 chế biến đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '3'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def transport_dh(request, input_id):  # 4 vận chuyển đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '4'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def done_dh(request, input_id):  #  5 hoàn thành đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '5'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")

