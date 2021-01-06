from django.db import models


# Create your models here.

class ZilTanimi(models.Model):
    GUN = [[0, 'Pazartesi'],
           [1, 'Salı'], [2, 'Çarşamba'],
           [3, 'Perşembe'], [4, 'Cuma'],
           [5, 'Cumartesi'],
           [6, 'Pazar'], ]

    dersbaslangicsaati = models.TimeField(verbose_name='Derslerin Başlangıç Saati', default='09:00', auto_now=False)
    toplanmasuresi = models.TimeField(verbose_name='Toplanma Süresi', default='00:10')
    ogretmenzilsuresi = models.TimeField(verbose_name='Öğretmen Ders Bildirim Zili', default='00:03')
    derssayisi = models.SmallIntegerField(verbose_name='Günlük Ders Sayısı', default=10)
    derssuresi = models.TimeField(verbose_name='Ders Süresi', default='00:40')
    tenefussuresi = models.TimeField(verbose_name='Tenefüs Süresi', default='00:10')
    oglenarasiders = models.SmallIntegerField(verbose_name='Öğlen Arası', default=6)
    oglenarasisuresi = models.TimeField(verbose_name='Öğlen Arası Süresi', default='00:45')
    zilgun = models.SmallIntegerField(verbose_name='Tanımlanan Günü', choices=GUN, default=0, unique=True)
    active = models.BooleanField(verbose_name='Aktif Pasif', default=False)
    published_date = models.DateTimeField(verbose_name='Eklenme Tarihi', auto_now_add=True)

    class Meta:
        abstract = True


class NormalOkul(ZilTanimi):

    class Meta:
        db_table = 'zildefault'
        ordering = ['zilgun']


class AksamOkul(ZilTanimi):
    class Meta:
        db_table = 'zilaksam'
        ordering = ['zilgun']

