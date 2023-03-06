from django.contrib import admin
from .models import Danhmuc, Mon, CTGia

# Register your models here.

class CTGiaAdmin(admin.ModelAdmin):
    list_display= ('maGia', 'size','giaSize')

class DMAdmin(admin.ModelAdmin):
    list_display= ('maDM', 'tenDM','hinhAnhDM')

class MonAdmin(admin.ModelAdmin):
    list_display= ('maMon', 'maDM', 'tenMon','hinhAnh','ngayCN','gia','get_sizes' ,'trangThaiMon')


admin.site.register(CTGia,CTGiaAdmin)
admin.site.register(Danhmuc,DMAdmin)
admin.site.register(Mon,MonAdmin)

