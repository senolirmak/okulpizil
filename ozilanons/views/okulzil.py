from django.shortcuts import render, redirect, get_object_or_404
from uretim.models import AksamOkul
from uretim.models import DersZamanlama, NormalOkul
from ozilanons.models import DuyuruData

from ozilanons.forms import ZilDataForm, AksamZilDataForm, DuyuruDataForm, ZilDurumForm
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import logout
from uretim.ziluret.ziluret import OkulZiliCal, ZilUret
from background_task import background

# Create your views here.
zilhesapla = ZilUret(NormalOkul)
zilcal = OkulZiliCal(DersZamanlama, DuyuruData)
xmelodi = {'okultip': 'normal', 'toplan': 'toplanma.mp3', 'ilk': 'ilk.mp3', 'ders': 'ders.mp3', 'cik': 'cik.mp3',
           'metin': None}

zilcal.zil_melodi(**xmelodi)


@background(schedule=5)
def feed_database(aktif, guncel):
    zilcal.aktif_set(aktif)
    zilcal.guncel_set(guncel)
    zilcal.vericek()
    print(zilcal.aktif_get())
    print(zilcal.guncel_get())
    zilcal.GunlukZilleriKur()


def index(request):
    return render(request, 'ayarlar/index.html')


def Giris(request):
    messages.success(request, 'Giriş Yapıldı')
    return render(request, 'registration/login.html')


def Cikis(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('login')


def ZilKapat(request):
    icerik = get_object_or_404(DuyuruData, id=1)
    form = ZilDurumForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik = form.save(commit=False)
        # icerik.zilaktif = 1
        icerik.user = request.user
        icerik.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('duyurumetin')
    return render(request, 'ayarlar/anonsduyuru.html', {'form': form})


def ZilTanimMenu(request):
    return render(request, 'ayarlar/zilayarmenu.html')


def ZilListView(request):
    ziltanimi = NormalOkul.objects.all()
    if ZilUret.kontrol.get('guncel', False):
        ZilUret.uziller.clear()
        zilhesapla.uret()
        zilhesapla.ders_zil_kayit(DersZamanlama)
        zilhesapla.kontrol.update({'guncel': False})
        zilcal.aktif_set(True)
        zilcal.guncel_set(True)
        feed_database(zilcal.aktif_get(), zilcal.guncel_get())
    context = {'ziltanimi': ziltanimi}
    return render(request, 'ayarlar/new_ayarlar_detail.html', context)


def ZilListViewAksam(request):
    ziltanimi = AksamOkul.objects.all()
    context = {'ziltanimi': ziltanimi}
    return render(request, 'ayarlar/new_ayarlar_detail.html', context)


"""class NormalZilTanimListesi(SingleTableView):
    model = NormalOkul
    table_class = ZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'
    table_pagination = {
        "per_page": 10
    }


class AksamZilTanimListesi(SingleTableView):
    model = AksamOkul
    table_class = AksamZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'"""


def nokulziltanimi_ekle(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            ZilUret.kontrol.update({'guncel': True})
            return redirect('zillistview')
    else:
        form = ZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def aokulziltanimi_ekle(request):
    if request.method == "POST":
        form = AksamZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            ZilUret.kontrol.update({'guncel': True})
            return redirect('zilayarmenu')
    else:
        form = AksamZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def nokulziltanimi_sil(request, id):
    icerik = get_object_or_404(NormalOkul, id=id)
    form = ZilDataForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik.delete()
        ZilUret.kontrol.update({'guncel': True})
        messages.success(request, 'İçerik silindi')
        return redirect("zillistview")
    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def nokulziltanimi_duzenle(request, id):
    icerik = get_object_or_404(NormalOkul, id=id)
    form = ZilDataForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik = form.save(commit=False)
        icerik.user = request.user
        icerik.published_date = datetime.now()
        icerik.save()
        ZilUret.kontrol.update({'guncel': True})
        messages.success(request, 'İçerik Güncellendi')
        return redirect('zillistview')
    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def anonsduyuru_duzenle(request):
    metin = get_object_or_404(DuyuruData, id=1)
    form = DuyuruDataForm(request.POST or None, request.FILES or None, instance=metin)
    if form.is_valid():
        metin = form.save(commit=False)
        metin.guncellendi = 1
        if metin.metin is not None:
            zilcal.bayrak_set(True)
            zilcal.metin_set(metin.metin)
            print(metin.metin)
            zilcal.job_duyuru(metin.metin)

        metin.user = request.user
        metin.save()
        zilcal.metin_sil()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('zilayarmenu')
    else:
        form = DuyuruDataForm()
    return render(request, 'ayarlar/anonsduyuru.html', {'form': form})


def duyurumetin_duzenle(request):
    metin = get_object_or_404(DuyuruData, id=1)
    form = DuyuruDataForm(request.POST or None, request.FILES or None, instance=metin)
    if form.is_valid():
        metin = form.save(commit=False)
        metin.user = request.user
        metin.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('duyurumetin')

    return render(request, 'ayarlar/anonsduyuru.html', {'form': form})
