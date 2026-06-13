from django.contrib import admin

# Register your models here.
from.models import Provinsi
#admin.site.register(Provinsi)
@admin.register(Provinsi)  # 3. Gunakan decorator untuk mendaftarkan model
class ProvinsiAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter


from.models import Kabkota
#admin.site.register(Provinsi)
@admin.register(Kabkota)  # 3. Gunakan decorator untuk mendaftarkan model
class KabkotaAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter


from.models import Kecamatan
#admin.site.register(Provinsi)
@admin.register(Kecamatan)  # 3. Gunakan decorator untuk mendaftarkan model
class KecamatanAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter


from.models import Desa
#admin.site.register(Provinsi)
@admin.register(Desa)  # 3. Gunakan decorator untuk mendaftarkan model
class DesaAdmin(admin.ModelAdmin):
    # Kolom apa saja yang mau ditampilkan di list halaman admin
    list_display = ('id', 'district_id', 'name', 'alt_name', 'latitude', 'longitude') 
 
    search_fields = ('name', 'alt_name')  # Kolom yang bisa dicari

    list_filter = ('name',)  # Kolom yang bisa difilter

from .models import NamaData, Datprof  # Benar
@admin.register(NamaData)
class NamaDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama')
    search_fields = ('nama',)

@admin.register(Datprof)
class DatprofAdmin(admin.ModelAdmin):
    list_display = ('id', 'provinsi', 'namadata','tahun', 'jumlah')
    search_fields = ('provinsi__name', 'namadata__nama', 'tahun')