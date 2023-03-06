from django.contrib import admin

from .models import CTDonHang, DonHang, KhuyenMai
# Register your models here.


class DHAdmin(admin.ModelAdmin):
    list_display= ('maDH', 'maKH','tongTien','ngayLap','trangThaiDH')

class CTDHAdmin(admin.ModelAdmin):
    list_display= ('maCTDH', 'maDH','maMon', 'giaMon','soLuong')

class KMAdmin(admin.ModelAdmin):
    list_display= ('maKM', 'tenKM','code', 'phantramKM','ngayHetHan','trangThai')


admin.site.register(DonHang,DHAdmin)
admin.site.register(CTDonHang,CTDHAdmin)
admin.site.register(KhuyenMai,KMAdmin)
