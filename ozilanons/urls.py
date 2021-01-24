from django.urls import path
from ozilanons.views import Giris, nokulziltanimi_duzenle, Cikis, nokulziltanimi_sil, ZilListView
from ozilanons.views import index, nokulziltanimi_ekle, aokulziltanimi_ekle, ZilTanimMenu, FilteredZilListView
from ozilanons.views import ZilListViewAksam, duyurumetin_duzenle, ZilKapat, anonsduyuru_duzenle

urlpatterns = [
    path('', Giris, name='login'),
    path('home/cikis', Cikis, name='cikis'),
    path('home/', index, name='index'),
    path('home/okul/', ZilTanimMenu, name='zilayarmenu'),
    path('home/okul/odata/', ZilListView, name='zillistview'),
    path('home/okul/oadata/', ZilListViewAksam, name='zillistviewaksam'),
    path('home/okul/new/', nokulziltanimi_ekle, name='okul_new'),
    path('home/okul/aksam/new/', aokulziltanimi_ekle, name='aksam_new'),
    path('home/okul/zil/<int:ders_gun>', FilteredZilListView, name='gunzillist'),
    path('home/okul/edit/<int:id>', nokulziltanimi_duzenle, name='guncelle'),
    path('home/okul/sil/<int:id>', nokulziltanimi_sil, name='sil'),
    path('home/okul/duyurumetin/', duyurumetin_duzenle, name='duyurumetin'),
    path('home/okul/anonsduyuru/', anonsduyuru_duzenle, name='anonsduyuru'),
    path('home/okul/duyurumetin/', ZilKapat, name='zilikapat'),

]

# path('home/okul/ozilaksamdata/', AksamZilDataListView.as_view(), name='ozilaksamdata'),
# path('home/okul/ozildata/', ZilDataListView.as_view(), name='ozildata'),
# path('home/okul/anonsduyuru/', anonsduyuru, name='anonsduyuru'),
# path('home/okul/new2/', new_post_zildata, name='new2'),
