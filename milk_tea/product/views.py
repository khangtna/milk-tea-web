from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from product.models import Danhmuc, Mon, CTGia, CTDanhGia
from .forms import danhGiaForm



def getAllProduct(request):
    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'count_All': Mon.objects.all().count()
    }

    return render(request, 'homepage/product/menu.html', context)


def getDMProduct(request, id):

    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True, maDM= id)
        
    }

    return render(request, 'homepage/product/menu.html', context)



def getDetailProduct(request,mon_id):

    # giamon= Mon.objects.filter(maMon= mon_id).values_list('gia', flat=True)
    # giasize= CTGia.objects.filter(maDM= dm_id).values_list('giaSize', flat=True)

    # total = sum(giamon) + sum(giasize)
    
    # mon = Mon.objects.get(trangThaiMon=True, maMon= mon_id)
    mon= get_object_or_404(Mon, pk= mon_id)
   
    m= get_object_or_404(CTGia ,pk= 14)
    l= get_object_or_404(CTGia ,pk= 15) 

    mon.sizeMon.add(m)
    mon.sizeMon.add(l)

    sizes= mon.sizeMon.all()

    danhgiaMon = CTDanhGia.objects.filter(maMon = mon_id)
    form = danhGiaForm()

    context={
        'mon': mon,
        'sizes':sizes,
        'danhgia': danhgiaMon,
        'form' : form,

    }

    if request.GET.get('size'):
        size= request.GET.get('size')
        # print(size)
        price= mon.get_product_price_by_size(mon_id,size)
        context['selected_size'] = size
        context['updated_price'] = price
        # print(price)
   
    return render(request, 'homepage/product/detailProduct.html', context)


def addReview(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        input = danhGiaForm(request.POST, request.FILES)

        input.is_valid()
        input.save()

        ob = float(input['rating'].value())
        mon = input['maMon'].value()
        print(mon)
        obmon = Mon.objects.get(maMon = mon)

        sldanhgia = CTDanhGia.objects.filter(maMon = mon)

        sum = 0.0
        for item in sldanhgia:
            sum += item.rating
        sum+= ob
        obmon.rating = (sum/(sldanhgia.count()+1))
        obmon.save()

        messages.success(request, f"Cảm ơn bạn đã đánh giá.")
        return redirect(url)
    return redirect('allmon')
