from django.db import models

class Provinsi(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'provinces'  # Menyesuaikan dengan nama tabel di SQL Anda
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Provinsi'

    def __str__(self):
        return self.name
# Create your models here.

class Kabkota(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.ForeignKey(
        'Provinsi', 
        on_delete=models.CASCADE, 
        db_column='province_id',  # Menyesuaikan nama kolom foreign key di database SQL
        related_name='kabkota_set'
    )
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'regencies'  # Menyesuaikan dengan nama tabel di SQL Anda
        verbose_name = 'Kabupaten/Kota'
        verbose_name_plural = 'Kabupaten/Kota'

    def __str__(self):
        return self.name
    

#district
class Kecamatan(models.Model):
    id = models.BigAutoField(primary_key=True)
    regency = models.ForeignKey(
        'Kabkota', 
        on_delete=models.CASCADE, 
        db_column='regency_id',  # Menyesuaikan nama kolom foreign key di database SQL
        related_name='kecamatan_set'
    )
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'districts'  # Menyesuaikan dengan nama tabel di SQL Anda
        verbose_name = 'Kecamatan'
        verbose_name_plural = 'Kecamatan'

    def __str__(self):
        return self.name
    

#villages
class Desa(models.Model):
    id = models.BigAutoField(primary_key=True)
    district = models.ForeignKey(
        'Kecamatan', 
        on_delete=models.CASCADE, 
        db_column='district_id',  # Menyesuaikan nama kolom foreign key di database SQL
        related_name='desa_set'
    )
    name = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255, default='', blank=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    class Meta:
        db_table = 'villages'  # Menyesuaikan dengan nama tabel di SQL Anda
        verbose_name = 'Desa/Kelurahan'
        verbose_name_plural = 'Desa/Kelurahan'

    def __str__(self):
        return self.name
    

    from django.db import models

class NamaData(models.Model):
    # Field 'id' otomatis dibuat oleh Django sebagai AutoField (Integer, Primary Key)
    nama = models.CharField(max_length=100)

    class Meta:
        db_table = 'namadata'  # Memastikan nama tabel di database sesuai request Anda

    def __str__(self):
        return self.nama

class Datprof(models.Model):
    # Foreign Key ke model Provinsi (tabel provinces)
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.CASCADE,
        db_column='provinsi_id',
        related_name='datprof_provinsi'
    )

    # Foreign Key ke model NamaData (tabel namadata)
    namadata = models.ForeignKey(
        NamaData,
        on_delete=models.CASCADE,
        db_column='namadata_id',
        related_name='datprof_namadata'
    )

    # Field Tahun (Integer)
    tahun = models.IntegerField()

    # Field Jumlah (Double Precision di PostgreSQL)
    jumlah = models.FloatField()

    class Meta:
        db_table = 'data_provinces'  # Menentukan nama tabel di PostgreSQL
        
    def __str__(self):
        return f"Data {self.namadata.nama} - {self.provinsi.id} ({self.tahun})"