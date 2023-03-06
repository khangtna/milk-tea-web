from django.shortcuts import render,redirect, get_object_or_404
from django.views import View

from product.models import Danhmuc, Mon, CTGia



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

    context={
        'mon': mon,
        'sizes':sizes

    }

    if request.GET.get('size'):
        size= request.GET.get('size')
        # print(size)
        price= mon.get_product_price_by_size(mon_id,size)
        context['selected_size'] = size
        context['updated_price'] = price
        # print(price)
   
    

    return render(request, 'homepage/product/detailProduct.html', context)



