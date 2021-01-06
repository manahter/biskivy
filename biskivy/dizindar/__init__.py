from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.event import EventDispatcher
from functools import partial
import os



"""

Tamamen kullanım dışı ŞUAN

bunu düzenleyeceğiz.
Dizinin içindeki dosyaları klasörleri tutacak.
İçerikten herhangi birşey değiştiğinde yeniden yükleyecek...

"""


class Didik(list):
    """
    Dizinin içindeki dosyaları tutar/takip eder
    """
    modified_time = 0
    """Last modified time, Json dosyasının, son değiştirilme zamanı takip edilir"""

    load = None
    """Metod, json değiştiğinde, defterdar'ın loadı işletilir"""

    def __init__(self, path, liste=[], **kwargs):
        """
        Muhimme, dizini okur. Okunan veri değiştikçe, değişkene aktarır
        Args:
            path: dizin yolu
            **kwargs:
        """
        super(Didik, self).__init__(liste)
        self.path = path
        self._load()
        Clock.schedule_interval(self.takip, 1)

    def _load(self):
        # Belirtilen dosya mevcut değilse, bitirilir
        if os.path.exists(self.path):
            # Dosya okunur
            data = os.listdir(self.path)
            super(Didik, self).__init__(data)

        if self.load:
            self.load()

    def takip(self, *args):
        try:
            if not os.path.exists(self.path):
                return
            t = os.path.getctime(self.path)
            if t != self.modified_time:
                self._load()
                self.modified_time = t
        except:
            return


class Dizindar(EventDispatcher):
    """
    Defterdar kayıtçıdır.
    didik:
        Defterdarın Data kayıtlarını tuttuğu defterdir. Json formatındadır.
        Defterde değişiklik olup olmadığı sürekli takip edilir.
        Örn; 'prefs/theme/button.json'  -> Buton widget'ı ile ilgili
              değerler bu defterde tutulur

    items:
        Mühimme defterindeki takip edilecek değişkenlerin listesidir.
        Bu değişkenler değiştiğinde, mühimme defteri ve self'deki değişken
        güncellenir.
        Örn; [renk_text, renk_inner, scale ...] -> self'deki renk_text
             değeri değiştiğinde, mühimmeye kaydedilir. Veya mühimmede
             bir değişiklik olduğunda, self'deki renk_text güncellenir.
    """

    didik = ObjectProperty()
    """Mühimme defteri. Defterdarın Data kayıtlarını tuttuğu defterdir. 
    Örn; 'prefs/paths.json'
    """

    items = ListProperty()
    """Kontrol edilecek değişkenler. Örneğin;
    """

    def __init__(self, *args, **kwargs):
        super(Dizindar, self).__init__(*args, **kwargs)
        self.load()

    def on_didik(self, caller, didik_name):
        if type(didik_name) is str:
            self.didik = Didik(didik_name)
            self.didik.load = self.didik_load

    def didik_load(self):
        """Muhimme'deki verileri oku / tekrar oku"""
        if self.didik is None:
            return

        for i in self.items:
            o = self.didik.get(i)
            if o:
                exec(f"self.{i} = {o}")

    def on_items(self, *args):
        """Defterdar listesi değiştiğinde, liste öğelerine bind ekler"""
        # Liste öğelerine BIND ekle. Herhangi birisi değiştiğinde, Defterdar, verileri json dosyasına kaydetsin
        for i in self.items:
            try:
                self.bind(**{i: partial(self._defter_tut, i)})
            except:
                print("Bu değişken bind yapmaya uygun değil", i)

        self.didik_load()

    def _defter_tut(self, key, caller, value):
        # Mühimme yoksa bitir
        if self.didik is None:
            return

        self.didik[key] = value
        self.didik.kayit()

    def load(self):
        """Kullanıcı başlangıç tanımlamaları için bu metodu kullanır"""

