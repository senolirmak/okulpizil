# Generated by Django 3.1.4 on 2021-01-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AksamOkul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dersbaslangicsaati', models.TimeField(default='09:00', verbose_name='Derslerin Başlangıç Saati')),
                ('toplanmasuresi', models.TimeField(default='00:10', verbose_name='Toplanma Süresi')),
                ('ogretmenzilsuresi', models.TimeField(default='00:03', verbose_name='Öğretmen Ders Bildirim Zili')),
                ('derssayisi', models.SmallIntegerField(default=10, verbose_name='Günlük Ders Sayısı')),
                ('derssuresi', models.TimeField(default='00:40', verbose_name='Ders Süresi')),
                ('tenefussuresi', models.TimeField(default='00:10', verbose_name='Tenefüs Süresi')),
                ('oglenarasiders', models.SmallIntegerField(default=6, verbose_name='Öğlen Arası')),
                ('oglenarasisuresi', models.TimeField(default='00:45', verbose_name='Öğlen Arası Süresi')),
                ('zilgun', models.SmallIntegerField(choices=[[0, 'Pazartesi'], [1, 'Salı'], [2, 'Çarşamba'], [3, 'Perşembe'], [4, 'Cuma'], [5, 'Cumartesi'], [6, 'Pazar']], default=0, unique=True, verbose_name='Tanımlanan Günü')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif Pasif')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'db_table': 'zilaksam',
                'ordering': ['zilgun'],
            },
        ),
        migrations.CreateModel(
            name='DersZamanlama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okul_turu', models.CharField(default='Örğün Eğitim', max_length=100, verbose_name='Okul Türü')),
                ('ders_gun', models.SmallIntegerField(choices=[[0, 'Pazartesi'], [1, 'Salı'], [2, 'Çarşamba'], [3, 'Perşembe'], [4, 'Cuma'], [5, 'Cumartesi'], [6, 'Pazar']], default=0, verbose_name='Tanımlanan Günü')),
                ('ders_no', models.SmallIntegerField(verbose_name='Ders No')),
                ('toplanma_saati', models.TimeField(verbose_name='Toplanma Saati')),
                ('ders_baslangic', models.TimeField(verbose_name='Dersin Başlangıç Saati')),
                ('ogretmen_saat', models.TimeField(verbose_name='Öğretmen Bildirim Saati')),
                ('ders_bitis', models.TimeField(verbose_name='Ders Bitiş Saati')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif Pasif')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'db_table': 'saat',
                'ordering': ['ders_gun', 'ders_no'],
            },
        ),
        migrations.CreateModel(
            name='NormalOkul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dersbaslangicsaati', models.TimeField(default='09:00', verbose_name='Derslerin Başlangıç Saati')),
                ('toplanmasuresi', models.TimeField(default='00:10', verbose_name='Toplanma Süresi')),
                ('ogretmenzilsuresi', models.TimeField(default='00:03', verbose_name='Öğretmen Ders Bildirim Zili')),
                ('derssayisi', models.SmallIntegerField(default=10, verbose_name='Günlük Ders Sayısı')),
                ('derssuresi', models.TimeField(default='00:40', verbose_name='Ders Süresi')),
                ('tenefussuresi', models.TimeField(default='00:10', verbose_name='Tenefüs Süresi')),
                ('oglenarasiders', models.SmallIntegerField(default=6, verbose_name='Öğlen Arası')),
                ('oglenarasisuresi', models.TimeField(default='00:45', verbose_name='Öğlen Arası Süresi')),
                ('zilgun', models.SmallIntegerField(choices=[[0, 'Pazartesi'], [1, 'Salı'], [2, 'Çarşamba'], [3, 'Perşembe'], [4, 'Cuma'], [5, 'Cumartesi'], [6, 'Pazar']], default=0, unique=True, verbose_name='Tanımlanan Günü')),
                ('active', models.BooleanField(default=False, verbose_name='Aktif Pasif')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'db_table': 'zildefault',
                'ordering': ['zilgun'],
            },
        ),
    ]