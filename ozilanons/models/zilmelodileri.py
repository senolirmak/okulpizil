from django.db import models
import os
from django.conf import settings

# Create your models here.


def mp3_path():
    PROJECT_ROOT = settings.BASE_DIR
    MP3FILES_FOLDER = os.path.join(PROJECT_ROOT, 'mp3file')
    return MP3FILES_FOLDER


class ZilMelodi(models.Model):
    melodi_id = models.SmallAutoField(primary_key=True)
    melodiad = models.TextField(verbose_name='Melodi Adı', max_length=200, choices=[['ogr', 'Öğretmen Giriş Zili'],
                                                                                    ['ilk', 'Öğenci Giriş Zili'],
                                                                                    ['cik', 'Çıkış Zili'],
                                                                                    ['istiklal', 'İstiklal Marşı']
                                                                                    ], unique=True)
    yol = models.FilePathField(path=mp3_path, recursive=False, verbose_name='Melodi Yolu', null=True)

    def __str__(self):
        return self.melodiad

    class Meta:
        db_table = 'melodipath'
