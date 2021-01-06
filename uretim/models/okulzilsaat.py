from django.db import models


# Create your models here.

class DersZamanlama(models.Model):
    GUN = [[0, 'Pazartesi'],
           [1, 'Salı'], [2, 'Çarşamba'],
           [3, 'Perşembe'], [4, 'Cuma'],
           [5, 'Cumartesi'],
           [6, 'Pazar'], ]
    okul_turu = models.CharField(max_length=100, verbose_name='Okul Türü', default='Örğün Eğitim')
    ders_gun = models.SmallIntegerField(verbose_name='Gün', choices=GUN, default=0)
    ders_no = models.SmallIntegerField(verbose_name='Ders No')
    toplanma_saati = models.TimeField(verbose_name='Toplanma Saati')
    ders_baslangic = models.TimeField(verbose_name='Dersin Başlangıç Saati')
    ogretmen_saat = models.TimeField(verbose_name='Öğretmen Bildirim Saati')
    ders_bitis = models.TimeField(verbose_name='Ders Bitiş Saati')
    active = models.BooleanField(verbose_name='Aktif Pasif', default=False)
    published_date = models.DateTimeField(verbose_name='Eklenme Tarihi', auto_now_add=True)

    class Meta:
        db_table = 'saat'
        ordering = ['ders_gun', 'ders_no', ]

    def __str__(self):
        return str(self.ders_gun)



