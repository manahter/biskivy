import json
import os

__copyright__   = 'Copyright 2020, Bildiri'
__license__     = 'GNU'
__version__     = '0.0.2'
__status__      = 'Geliştiriliyor..'
__date__        = "16.05.2020"
__isim__        = "Bildiri"

#__author__      = 'ÜÇN'
#__authors__     = ["O", "BU", "ŞU"]
#__credits__     = ['üçn', 'ova', "han"]
#__maintainer__  = 'üçn'
#__contact__     = '543 630 xx xx'
#__email__       = 'üçn@gmail.com'


'''
bildiri.py ile aynı konumda bulunan, 
ayar.json dosyasının içindeki
{   "bla": bla, 
    "bla": bla, 
    "bildiri": 1 -> bu kısım okunur
}
'''
yol = "{}/ayar.json".format(os.path.dirname(__file__))


class Renk:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'


class Bildiri:

    @classmethod
    def bayrak_oku(cls):
        """
        Bayraklar:
            0 -> Ekrana Basma
            1 -> Ekrana Bas
        :return:
        """
        cls.ayar_dosyasi_kontrol()

        with open(yol) as dosya:
            return json.load(dosya).get("bildiri", 0)

    @classmethod
    def bayrak_yaz(cls, val):
        cls.ayar_dosyasi_kontrol()

        with open(yol) as dosya:
            ayarlar = json.load(dosya)

        ayarlar["bildiri"] = val

        with open(yol, 'w', encoding='utf-8') as dosya:
            json.dump(ayarlar, dosya, ensure_ascii=False, indent=4)

    @classmethod
    def ayar_dosyasi_kontrol(cls):
        """ayar.json dosyası mevcut değilse oluştur."""

        ayarlar = {"bildiri": 1}

        if not os.path.exists(yol):
            with open(yol, 'w', encoding='utf-8') as dosya:
                json.dump(ayarlar, dosya, ensure_ascii=False, indent=4)
            Bildiri.uyari("Bildiri", "Ayar dosyası eksik olduğundan, yenisi oluşturuldu -> {}".format(yol))

    @classmethod
    def bilgi(cls, hatip, mesaj):
        cls.taslak("BiLGi", Renk.GREEN, hatip, mesaj)

    @classmethod
    def bilgi_gri(cls, hatip, mesaj):
        cls.taslak("BiLGi", Renk.GREY, hatip, mesaj)

    @classmethod
    def uyari(cls, hatip, mesaj):
        cls.taslak("UYARI", Renk.YELLOW, hatip, mesaj)

    @classmethod
    def hata(cls, hatip, mesaj):
        cls.taslak("HATA", Renk.RED, hatip, mesaj)

    @classmethod
    def ipucu(cls, hatip, mesaj):
        cls.taslak("iPUCU", Renk.BLUE, hatip, mesaj)

    @classmethod
    def taslak(cls, tip, renk, hatip, mesaj):
        if cls.bayrak_oku():
            print("[{}{}{: ^7s}{}] [{:12}] {}".format(Renk.BOLD, renk, tip, Renk.END, hatip, mesaj))
