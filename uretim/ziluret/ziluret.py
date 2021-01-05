import os
import sys
import time
from datetime import datetime, timedelta
import pygame
import schedule
from django.conf import settings
from gtts import gTTS


class ZilUret:
    kontrol = {'okultip': 'normal', 'guncel': False}
    uziller = list()

    def __init__(self, _ZilData):
        self.ziltanim = _ZilData
        self.dveri = list()
        self.veri = dict()

    def tanimveri(self):
        self.dveri = self.ziltanim.objects.filter(active=True)
        return self.dveri

    @classmethod
    def guncel_get(cls):
        cls.__class__.kontrol.get('guncel', False)

    @classmethod
    def guncel_set(cls, guncel):
        cls.__class__.kontrol.update({'guncel': guncel})

    @classmethod
    def veri_sil(cls):
        cls.__class__.uziller.clear()

    @staticmethod
    def h_saat(zaman_ts):
        hours, artan = divmod(zaman_ts, 3600)
        minutes, seconds = divmod(artan, 60)
        if hours > 23:
            hours -= 24

        d1 = datetime(2000, 1, 1, int(hours), int(minutes), 0)
        return d1.strftime('%H:%M')

    def donustur_saat(self, ilk_ts, ders_ts, cik_ts):
        ilk = self.h_saat(ilk_ts)
        ders = self.h_saat(ders_ts)
        cik = self.h_saat(cik_ts)
        return ilk, ders, cik

    @staticmethod
    def toplam_saniye(sure):
        sa, dk, sn = str(sure).split(':')
        saat = timedelta(hours=int(sa), minutes=int(dk), seconds=0)
        return saat.total_seconds()

    def oglensonrasi(self, oglenarasisuresi, ssonsaat):
        oglen_saniye = self.toplam_saniye(oglenarasisuresi)
        osson_saniye = self.toplam_saniye(ssonsaat)
        _sure = oglen_saniye + osson_saniye
        saat = self.h_saat(_sure)
        return saat

    def toplan(self, okulbaslamazaman, toplanmasuresi):
        toplan_saniye = self.toplam_saniye(okulbaslamazaman)
        tsures_saniye = self.toplam_saniye(toplanmasuresi)
        _sure = abs(toplan_saniye - tsures_saniye)
        saat = self.h_saat(_sure)
        return saat

    @classmethod
    def ders_zil_get(cls, *args):
        okultip, dersgun, dersno = args
        for guz in cls.uziller:
            if guz.get('okultip', None) == okultip:
                if guz.get('dersgun', None) == dersgun:
                    if guz.get('dersno', None) == dersno:
                        return guz

    @classmethod
    def gunzil_say_get(cls, *args):
        okultip, dersgun = args
        say = 0
        for guz in cls.uziller:
            if guz.get('okultip', None) == okultip:
                if guz.get('dersgun', None) == dersgun:
                    say += 1

        return say

    @classmethod
    def ders_zil_gun_get(cls):
        return cls.uziller

    @classmethod
    def ders_zil_kayit(cls, zamanlar):
        if cls.kontrol.get('guncel', False):
            zamanlar.objects.all().delete()
            for guz in cls.uziller:
                veri = zamanlar(
                    okul_turu=guz.get('okultip', None),
                    ders_gun=guz.get('dersgun', None),
                    ders_no=guz.get('dersno', None),
                    toplanma_saati=guz.get('toplan', None),
                    ders_baslangic=guz.get('ilk', None),
                    ogretmen_saat=guz.get('ders', None),
                    ders_bitis=guz.get('cik', None),
                    active=True,
                    published_date=datetime.now(),
                )
                veri.save()

    def derszilihesapla(self, z, f_veri):
        if z == 1:
            _ztoplan = self.toplan(f_veri.dersbaslangicsaati, f_veri.toplanmasuresi)
        else:
            _ztoplan = '00:00'

        oglen_dersii = f_veri.oglenarasiders
        oglen_saniye = self.toplam_saniye(f_veri.oglenarasisuresi)
        obast_saniye = self.toplam_saniye(f_veri.dersbaslangicsaati)
        suret_saniye = self.toplam_saniye(f_veri.derssuresi)
        tenft_saniye = self.toplam_saniye(f_veri.tenefussuresi)
        ogrtt_saniye = self.toplam_saniye(f_veri.ogretmenzilsuresi)

        if (z > oglen_dersii) and (oglen_dersii != 0 and oglen_dersii is not None):
            obast_saniye += (oglen_saniye - tenft_saniye)

        ilk = ((obast_saniye + (z - 1) * (suret_saniye + tenft_saniye)) - ogrtt_saniye)
        ders = (obast_saniye + (z - 1) * (suret_saniye + tenft_saniye))
        cik = obast_saniye + z * suret_saniye + (z - 1) * tenft_saniye

        _ilk, _ders, _cik = self.donustur_saat(ilk, ders, cik)
        _zilgun = f_veri.zilgun
        keys = 'okultip', 'dersgun', 'dersno', 'toplan', 'ilk', 'ders', 'cik'
        ziller = dict.fromkeys(keys)

        ziller['okultip'] = 'normal'
        ziller['dersgun'] = _zilgun
        ziller['dersno'] = z
        ziller['toplan'] = _ztoplan
        ziller['ilk'] = _ilk
        ziller['ders'] = _ders
        ziller['cik'] = _cik
        self.__class__.uziller.append(ziller)

    def tanimsizgun(self):
        hitanimligun = list()
        pzt_veri = dict()
        for g in self.tanimveri():
            if g.zilgun in [0, 1, 2, 3, 4]:
                hitanimligun.append(g.zilgun)

        for g in self.tanimveri():
            if g.zilgun == 0:
                pzt_veri = g

        return pzt_veri, set(hitanimligun).symmetric_difference({0, 1, 2, 3, 4})

    def uret(self):
        try:
            pztx_veri, manup_veri = list(self.tanimsizgun())
            for g in self.tanimveri():
                for i in range(1, g.derssayisi + 1):
                    if g.zilgun in [0, 1, 2, 3, 4]:
                        self.derszilihesapla(i, g)

                    if g.zilgun in [5, 6]:
                        self.derszilihesapla(i, g)

            for gbf in manup_veri:
                pztx_veri.zilgun = gbf
                for i in range(1, pztx_veri.derssayisi + 1):
                    self.derszilihesapla(i, pztx_veri)

        except TypeError:
            print("veri üretimi hatalı")


class OkulZiliCal:
    keys = 'okultip', 'toplan', 'ilk', 'ders', 'cik', 'metin'
    melodi = dict.fromkeys(keys)

    def __init__(self, _zamanTable, _anons,  _okultip='normal'):
        self._aktif = False
        self._guncel = False
        self._metin = None
        self._bayrak = False
        self._okultip = _okultip
        self._zamantable = _zamanTable
        self._anons = _anons
        self._veri = self._zamantable.objects.filter(okul_turu=self._okultip)
        self._projedir = settings.BASE_DIR

    def vericek(self):
        if self.guncel_get():
            self._veri = self._zamantable.objects.filter(okul_turu=self._okultip)

    def metin_sil(self):
        veri = self._anons.objects.get(id=1)
        veri.metin = None
        veri.guncellendi = False
        veri.save()

    def aktif_get(self):
        return self._aktif

    def guncel_get(self):
        return self._guncel

    def aktif_set(self, aktif):
        self._aktif = aktif

    def metin_set(self, metin):
        self._metin = metin

    def bayrak_set(self, bayrak):
        self._bayrak = bayrak

    def guncel_set(self, aktif):
        self._guncel = aktif

    def derssayisi_get(self, _gun):
        _gun = _gun
        _veri = self._veri.filter(ders_gun=_gun)
        return len(_veri)

    def derszili_get(self, *args):
        gun, ders_no = args
        toplan, ilk, ders, cik = ('00:00:00', '00:00:00', '00:00:00', '00:00:00')
        veri = self._veri.filter(ders_gun=gun, ders_no=ders_no)
        for d in veri:
            toplan = str(d.toplanma_saati)[:5]
            ilk = str(d.ogretmen_saat)[:5]
            ders = str(d.ders_baslangic)[:5]
            cik = str(d.ders_bitis)[:5]
        return toplan, ilk, ders, cik

    @classmethod
    def zil_melodi(cls, **kwargs):
        f_veri = {}
        for key, value in kwargs.items():
            f_veri[key] = value
        cls.melodi = f_veri.copy()

    def job_duyuru(self, metin):
        try:
            tts = gTTS(metin, lang="tr")
            tts.save(str(self._projedir)+'/mp3file/anons.mp3')
            self.job_play('anons.mp3')
            self._bayrak = False
            self.metin_sil()
            time.sleep(3)
            os.remove(str(self._projedir) + '/mp3file/anons.mp3')
        except RuntimeError:
            print("Google gTTS kullanılamıyor")
        finally:
            print('finall')

    def job_play(self, music):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self._projedir, "mp3file", music))
        pygame.mixer.music.play()
        if music == 'anons.mp3':
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    def job_toplanma(self):
        self.job_play(self.melodi.get('toplan', 'toplanma.mp3'))

    def job_ilk(self):
        self.job_play(self.melodi.get('ilk', 'ilk.mp3'))

    def job_ders(self):
        self.job_play(self.melodi.get('ders', 'ders.mp3'))

    def job_cikis(self):
        self.job_play(self.melodi.get('cikis', 'cik.mp3'))

    @staticmethod
    def Sonraki_Zil(time0):
        sa, dk = str(time0)[:5].split(':')
        t0 = timedelta(hours=int(sa), minutes=int(dk), seconds=0)
        simdi = datetime.now()
        h0 = simdi.hour
        m0 = simdi.minute
        s0 = simdi.second
        t1 = timedelta(hours=int(h0), minutes=int(m0), seconds=int(s0))
        return t0 >= t1

    def GunlukZilleriKur(self):
        now = datetime.now()
        gun = int(now.strftime("%w")) - 1
        if gun == -1:
            gun = 6
        while self.aktif_get():
            if self._bayrak:
                self.job_duyuru(self._metin)

            for k in range(1, self.derssayisi_get(gun) + 1):
                toplan, ilk, ders, cik = self.derszili_get(gun, k)
                if self.Sonraki_Zil(toplan):
                    schedule.every().day.at(toplan).do(self.job_toplanma)
                    print("Toplan Zil, {}. Ders".format(k))
                    break

                if self.Sonraki_Zil(ilk) and (self.Sonraki_Zil(cik)):
                    schedule.every().day.at(ilk).do(self.job_ilk)
                    print("İlk Zil, {}. Ders".format(k))
                    break

                if self.Sonraki_Zil(ders) and not (self.Sonraki_Zil(ilk)):
                    schedule.every().day.at(ders).do(self.job_ders)
                    print("Ders Zil, {}. Ders".format(k))
                    break

                if self.Sonraki_Zil(cik) and not (self.Sonraki_Zil(ders)):
                    schedule.every().day.at(cik).do(self.job_cikis)
                    print("Cık Zil, {}. Ders".format(k))
                    if k < self.derssayisi_get(gun) + 1:
                        break

                if k == self.derssayisi_get(gun):
                    self.aktif_set(False)

            # schedule.every().day.at("22:00").do(self.kapat)
            schedule.run_pending()
            time.sleep(5)
