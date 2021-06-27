from django.db import models
from django.urls import reverse

from ...common.models import WorkOrderAbstractModel


class SLD(WorkOrderAbstractModel):

    # Burdaki isimlendirmeler js tarafında da aynı şekilde olmalıdır!
    # Herhanbi bi değişiklikte dikkatli olunmalı
    DOOR_TYPES = (
        ('th_standart', 'STANDART TEK HAREKETLİ'),
        ('ts_th_standart', 'STANDART TEK SBT. + TEK HRK.'),
        ('ih_standart', 'STANDART İKİ HAREKETLİ'),
        ('is_ih_standart', 'STANDART İKİ SBT. + İKİ HRK.'),
        ('th_cam', 'CAM - TEK HAREKETLİ'),
        ('ts_th_cam', 'CAM - TEK SBT. + TEK HRK.'),
        ('ih_cam', 'CAM - İKİ HAREKETLİ'),
        ('is_ih_cam', 'CAM - İKİ SBT. + İKİ HRK.'),
        ('ih_teleskop', 'TELESKOPİK - İKİ HAREKETLİ'),
        ('ih_is_teleskop', 'TELESKOPİK - İKİ HRK. + İKİ SBT.'),
        ('dh_teleskop', 'TELESKOPİK - DÖRT HAREKETLİ'),
        ('dh_is_teleskop', 'TELESKOPİK - DÖRT HRK. + İKİ SBT.'),
    )

    OPTIONS_LIST = {
        'konum_anahtari_standart': 'Konum Anahtarı Standart',
        'konum_anahtarı_sivaustu': 'Konum Anahtarı Sıva Üstü',
        'el_terminali': 'El Terminali',
        'acil_stop': 'Acil Stop',
        'elektronik_kilit': 'Elektronik Kilit',
        'batarya': 'Batarya',
    }
    RADAR_ACTIVATION_LIST = {
        'mikrodalga_radar': 'Mikrodalga Radar',
        'combine_safety_activation': 'Combine Safety - Activation',
        'yaklasim_sensoru': 'Yaklaşım Sensörü',
        'emniyet_fotoseli': 'Emniyet Fotoseli',
    }
    glass = models.CharField('Cam', max_length=25)
    color = models.CharField('Renk', max_length=20)
    opening_direction = models.CharField('Açılış Yönü', max_length=3,
                                         choices=(('sag', 'SAĞ'), ('sol', 'SOL')), null=True, blank=True)
    ustluk = models.BooleanField('Üstlük Var Mı?', default=False)
    door_type = models.CharField('Kapı Tipi', choices=DOOR_TYPES, max_length=30)
    pass_width = models.PositiveSmallIntegerField('Geçiş Genişliği')
    pass_height = models.PositiveSmallIntegerField('Geçiş Yüksekliği')
    total_width = models.PositiveSmallIntegerField('Toplam Genişlik', null=True, blank=True)
    total_height = models.PositiveSmallIntegerField('Toplam Yükseklik', null=True, blank=True)
    mechanism_width = models.PositiveSmallIntegerField('Mekanizma Genişliği', null=True, blank=True)

    # opsiyonlar ve radar aktivasyonları aralarında boş bırakılarak "*_LIST" içerisindeki ilk verilerden olusturulmalı
    # ornek: "acil_stop batarya"
    options = models.CharField('Opsiyonlar', blank=True, null=True, max_length=250)
    radar_activations = models.CharField('RADAR ve AKTİVASYON SEÇENEKLERİ', blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = 'SLD'
        verbose_name_plural = 'SLDs'

    def get_absolute_url(self):
        return reverse('sld:detail', kwargs={'id': self.id})

    @property
    def get_display_options(self):
        if self.options:
            return [self.OPTIONS_LIST.get(option) for option in self.options.split(' ')]
        return None

    @property
    def get_display_radar_activations(self):
        if self.radar_activations:
            return [self.RADAR_ACTIVATION_LIST.get(radar) for radar in self.radar_activations.split(' ')]
        return None

    def door(self):
        return self.door_type.split('_')[-1]

    def wing(self):
        for i in self.DOOR_TYPE:
            return i if i == self.door_type else ''

    def get_slider_wing_count(self):
        """
        Kayar kanat sayısını hesaplama
        """
        if 'th' in self.door_type:
            return 1
        elif 'ih' in self.door_type:
            return 2
        elif 'dh' in self.door_type:
            return 4

    def get_fixed_wing_count(self):
        """
        Sabit kanat sayısını hesaplama
        """
        if 'ts' in self.door_type:
            return 1
        elif 'is' in self.door_type:
            return 2
        else:
            return 0

    def get_wings_info(self):
        """
        Kanat sayılarını alma
        """
        return self.get_slider_wing_count(), self.get_fixed_wing_count()
