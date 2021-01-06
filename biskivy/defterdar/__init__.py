from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.clock import Clock
from kivy.event import EventDispatcher
from functools import partial
import os


module_path = os.path.dirname(__file__)
"""Aradığımız prefs doslarının tutulduğu dizini, bu modülün dizinine koyduk"""


class Muhimme(dict):
    """Muhimme, Json dosyasını sözlük şeklinde okur. Okunan veri değiştikçe, aynı dosyaya veriyi kaydeder."""

    import json
    #module_path = ""
    #"""json dosyası veya dizin yolu"""

    splitter = "/"
    """fullget metoduna verilen, 
    fullkey parametresi, 
    splitter karakteri ile bölünür"""

    modified_time = 0
    """Last modified time, Json dosyasının, son değiştirilme zamanı takip edilir"""

    load = None
    """Metod, json değiştiğinde, defterdar'ın loadı işletilir"""

    def __init__(self, path, sozluk={}, **kwargs):
        """
        Muhimme, Json dosyasını sözlük şeklinde okur. Okunan veri değiştikçe, aynı dosyaya veriyi kaydeder.
        Args:
            path: json dosyasının yolu
            **kwargs:
        """
        super(Muhimme, self).__init__(sozluk, **kwargs)
        self.path = path
        self._load(**kwargs)
        Clock.schedule_interval(self.takip, 1)

    def _load(self, **kwargs):
        # Belirtilen dosya mevcut değilse, oluşturulur

        if not os.path.exists(self.path):
            a = self.kayit({})
            if not a:
                # Böyle yapmazsak, Clock çalışmıyor
                return

        # Dosya okunur
        with open(self.path) as json_file:
            data = self.json.load(json_file)
            super(Muhimme, self).__init__(data, **kwargs)

        if self.load:
            self.load()

    def fullget(self, fullkey: str, value=None) -> object:
        """
        Args:
            fullkey: alt alta sözlük key'leri aralarına 'self.splitter' koyularak girilebilir.
                Örneğin: fullkey = "dict_key0/dict_key1/dict_key2"
                Bu şunu ifade eder; dict_key0'in altındaki, dict_key1'in altındaki, dict_key2'nin value'sini isterim
            value:
                fullkey yok ise, value geri döner.
        Returns:
            fullkeys_value or value:
        """

        # fullkey'i parçalara ayırıyoruz. "" -> şeklinde boş olanları siliyoruz
        a = list(filter(None, fullkey.split(self.splitter)))

        # fullkeys_value'i buna koyuyoruz
        veri = self
        for i in a:
            veri = veri.get(i)

        # Varsa fullkeys_value, yoksa value döndürüyoruz.
        return veri or value

    def fullset(self, fullkey: str, value) -> None:
        """
        Args:
            fullkey: alt alta sözlük key'leri aralarına 'self.splitter' koyularak girilebilir.
                Örneğin: fullkey = "dict_key0/dict_key1/dict_key2"
                Bu şunu ifade eder; dict_key0'in altındaki, dict_key1'in altındaki, dict_key2'nin value'sini isterim
            value:
                fullkey'e, value değeri gönderilir.
        """

        # fullkey'i parçalara ayırıyoruz
        a = fullkey.split(self.splitter)

        # fullkeys_value'i buna koyuyoruz
        veri = self
        for i in a[:-1]:
            veri = veri.get(i)

        veri[a[-1]] = value

    def kayit(self, data=None):
        try:
            with open(self.path, 'w') as outfile:
                self.json.dump(data or self, outfile, indent=4)
            return True
        except:
            return False

    def takip(self, *args):
        try:
            t = os.path.getctime(self.path)
            if t != self.modified_time:
                self._load()
                self.modified_time = t
        except:
            return


class Defterdar(EventDispatcher):
    """
    Defterdar kayıtçıdır.
    muhimme:
        Defterdarın Data kayıtlarını tuttuğu defterdir. Json formatındadır.
        Defterde değişiklik olup olmadığı sürekli takip edilir.
        Örn; 'prefs/theme/button.json'  -> Buton widget'ı ile ilgili
              değerler bu defterde tutulur

    defter_listesi:
        Mühimme defterindeki takip edilecek değişkenlerin listesidir.
        Bu değişkenler değiştiğinde, mühimme defteri ve self'deki değişken
        güncellenir.
        Örn; [renk_text, renk_inner, scale ...] -> self'deki renk_text
             değeri değiştiğinde, mühimmeye kaydedilir. Veya mühimmede
             bir değişiklik olduğunda, self'deki renk_text güncellenir.
    """

    muhimme = ObjectProperty()
    """Mühimme defteri. Defterdarın Data kayıtlarını tuttuğu defterdir. 
    Örn; 'prefs/paths.json'
    """

    defter_listesi = ListProperty()
    """Kontrol edilecek değişkenler. Örneğin;
    -> [renk_text, renk_inner, scale ...]"""

    def __init__(self, *args, **kwargs):
        super(Defterdar, self).__init__(*args, **kwargs)
        self.load()

    def on_muhimme(self, caller, muhimme_name):
        if type(muhimme_name) is str:
            p = os.path.join(module_path, muhimme_name)
            self.muhimme = Muhimme(p)
            self.muhimme.load = self.muhimme_load

    def muhimme_load(self):
        """Muhimme'deki verileri oku / tekrar oku"""
        if self.muhimme is None:
            return

        for i in self.defter_listesi:
            o = self.muhimme.get(i)
            if o:
                if type(o) is str:
                    exec(f"self.{i} = '{o}'")
                else:
                    exec(f"self.{i} = {o}")

    def on_defter_listesi(self, *args):
        """Defterdar listesi değiştiğinde, liste öğelerine bind ekler"""
        # Liste öğelerine BIND ekle. Herhangi birisi değiştiğinde, Defterdar, verileri json dosyasına kaydetsin
        for i in self.defter_listesi:
            try:
                self.bind(**{i: partial(self._defter_tut, i)})
            except:
                print("Bu değişken bind yapmaya uygun değil", i)

        self.muhimme_load()

    def _defter_tut(self, key, caller, value):
        # Mühimme yoksa bitir
        if self.muhimme is None:
            return

        self.muhimme[key] = value
        self.muhimme.kayit()

    def load(self):
        """Kullanıcı başlangıç tanımlamaları için bu metodu kullanır"""


#class Arsiv(list):
#    [
#        "Dosya_yolu",
#        "Dosya_adı",
#        "Uzantısı",
#        "Değiştirilme Tarihi"
#    ]
#
#
#class DizinTakipci(EventDispatcher):
#    """Bir dizin içindeki dosyaların değişip değişmediğini takip eder."""
#
#    dizin = StringProperty()
#
#    def __init__(self, *args, **kwargs):
#        super(DizinTakipci, self).__init__(*args, **kwargs)
#        self.load()
#
#    def on_dizin(self, *args):
#        pass
#
#    def load(self):
#        """Kullanıcı başlangıç tanımlamaları için bu metodu kullanır"""