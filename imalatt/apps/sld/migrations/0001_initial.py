# Generated by Django 2.2 on 2021-02-02 18:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=10, verbose_name='CRM NO')),
                ('company_name', models.CharField(max_length=150, verbose_name='Firma')),
                ('billing_address', models.CharField(max_length=80, verbose_name='Fatura Adresi')),
                ('delivery_address', models.CharField(max_length=80, verbose_name='Sevk Adresi')),
                ('delivery_date', models.DateField(verbose_name='Teslim Tarihi')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('delivery_type', models.CharField(choices=[('Kapıda', 'Kapıda'), ('Ambar', 'Ambar'), ('Atölye', 'Atölye')], max_length=10, verbose_name='Teslim Şekli')),
                ('has_chest', models.BooleanField(verbose_name='Sandıklı Mı?')),
                ('notes', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Notlar')),
                ('drawing', models.CharField(max_length=200, verbose_name='Hazırlayan')),
                ('control', models.CharField(blank=True, max_length=40, null=True, verbose_name='Kontrol')),
                ('manufacturing_chief', models.CharField(blank=True, max_length=40, null=True, verbose_name='İmalat Şefi')),
                ('glass', models.CharField(max_length=25, verbose_name='Cam')),
                ('color', models.CharField(max_length=20, verbose_name='Renk')),
                ('opening_direction', models.CharField(blank=True, choices=[('sag', 'SAĞ'), ('sol', 'SOL')], max_length=3, null=True, verbose_name='Açılış Yönü')),
                ('ustluk', models.BooleanField(default=False, verbose_name='Üstlük Var Mı?')),
                ('door_type', models.CharField(choices=[('th_standart', 'STANDART TEK HAREKETLİ'), ('ts_th_standart', 'STANDART TEK SBT. + TEK HRK.'), ('ih_standart', 'STANDART İKİ HAREKETLİ'), ('is_ih_standart', 'STANDART İKİ SBT. + İKİ HRK.'), ('th_cam', 'CAM - TEK HAREKETLİ'), ('ts_th_cam', 'CAM - TEK SBT. + TEK HRK.'), ('ih_cam', 'CAM - İKİ HAREKETLİ'), ('is_ih_cam', 'CAM - İKİ SBT. + İKİ HRK.'), ('ih_teleskop', 'TELESKOPİK - İKİ HAREKETLİ'), ('ih_is_teleskop', 'TELESKOPİK - İKİ HRK. + İKİ SBT.'), ('dh_teleskop', 'TELESKOPİK - DÖRT HAREKETLİ'), ('dh_is_teleskop', 'TELESKOPİK - DÖRT HRK. + İKİ SBT.')], max_length=30, verbose_name='Kapı Tipi')),
                ('pass_width', models.PositiveSmallIntegerField(verbose_name='Geçiş Genişliği')),
                ('pass_height', models.PositiveSmallIntegerField(verbose_name='Geçiş Yüksekliği')),
                ('total_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Toplam Genişlik')),
                ('total_height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Toplam Yükseklik')),
                ('mechanism_width', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Mekanizma Genişliği')),
                ('options', models.CharField(blank=True, max_length=250, null=True, verbose_name='Opsiyonlar')),
                ('radar_activations', models.CharField(blank=True, max_length=250, null=True, verbose_name='RADAR ve AKTİVASYON SEÇENEKLERİ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SLD',
                'verbose_name_plural': 'SLDs',
            },
        ),
    ]