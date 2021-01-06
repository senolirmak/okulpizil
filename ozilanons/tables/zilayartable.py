import django_tables2 as tables

from uretim.models import NormalOkul, AksamOkul


class ZilayarTable(tables.Table):

    class Meta:
        model = NormalOkul
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'zilgun', 'active',)

        exclude = ('published_date', 'id', )
        order_by = 'zilgun'


"""class GunZilTable(tables.Table):

    class Meta:
        model = DersZamanlama
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('ders_no',
                    'toplanma_saati', 'ders_baslangic', 'ogretmen_saat', 'ders_bitis',)

        exclude = ('published_date', 'id', )
        order_by = 'zilgun'"""


class AksamZilayarTable(tables.Table):
    class Meta:
        model = AksamOkul
        template_name = 'django_tables2/bootstrap.html'

        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'zilgun', 'active',)

        exclude = ('published_date', 'id',)
        order_by = 'zilgun'
