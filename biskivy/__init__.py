"""
.. versionchanged:: 18.05.2020
    Verisyon takip tarihi eklendi

.. versionchanged:: 23.05.2020
    Modülün adı; 'biskivy' olarak düzenlendi
    Blender Style in Kivy
    Modullerin yerleri düzenlendi
"""

import os
import sys
from kivy.logger import Logger
from kivy.lang import Builder

import biskivy.factory_registers    # Temel Widget'larımız otomatik kayıt edilir

from biskivy.prefs import prefs     # Temel Ayarlarımız yüklenir
from biskivy.ops import ops         # Temel Operatörlerimiz yüklenir

__version__ = "0.1.0"
"""BisKivy version."""

path = os.path.dirname(__file__)
"""Path to BisKivy package directory."""

# Mevcut modül dosyalarımız, sisteme eklenir ### Düzenle
sys.path.append(path)

images_path = os.path.join(path, f"images{os.sep}")
"""Path to images directory."""

Logger.info(f"BisKivy: Blender Style in Kivy Installed")
Logger.info(f"BisKivy: v{__version__}")
Logger.info(f"BisKivy: Installed at '{path}'")


##################################################
class __Empty:
    pass


class IconPaths:
    wi_min = f"{images_path}wi_min.png"
    wi_max = f"{images_path}wi_max.png"
    pinned = f"{images_path}pinned.png"
    unpinned = f"{images_path}unpinned.png"
    sizer = f"{images_path}sizer.png"
    mv = f"{images_path}mv.png"
    selectmenu = f"{images_path}selectmenu.png"
    panel_opened = f"{images_path}panel_opened.png"
    panel_closed = f"{images_path}panel_closed.png"
    sayac_artir = f"{images_path}sayac_artir.png"
    sayac_azalt = f"{images_path}sayac_azalt.png"
    menyu_opened = f"{images_path}menyu_opened.png"
    menyu_closed = f"{images_path}menyu_closed.png"
    random_renk = f"{images_path}random_renk.png"
    damlalik = f"{images_path}damlalik.png"
    sb_dik = f"{images_path}sb_dik.png"
    renk = f"{images_path}renk.png"
    trans = f"{images_path}trans.png"
    menu = f"{images_path}menu.png"
    azalt = f"{images_path}azalt.png"
    arti = f"{images_path}arti.png"
    carpi = f"{images_path}carpi.png"
    eksi = f"{images_path}eksi.png"
    artir = f"{images_path}artir.png"
    locked = f"{images_path}locked.png"
    tutac = f"{images_path}tutac.png"

bkv = __Empty()
bkv.prefs = prefs
#bkv.paths = prefs.paths
bkv.paths = __Empty()
bkv.paths.icons = IconPaths()
##################################################

bkv.ops = ops

Builder.load_string("""
#: import bkv biskivy.bkv

####################################### Bulanıklık Sorununu çözmek için (ScrollView Kullanınca oluşan bulanıklık sorun)
#<Label@Label>:
#    on_texture:
#        if self.texture: self.texture.min_filter='nearest'
#        if self.texture: self.texture.mag_filter='nearest'
#        
#<TextInput@TextInput>:
#    on_size:
#        # Bulanıklık sorununu engelle
#        for i in self._lines_labels: i.min_filter='nearest' 
#        for i in self._lines_labels: i.mag_filter='nearest' 
#    on_text:
#        # Bulanıklık sorununu engelle
#        for i in self._lines_labels: i.min_filter='nearest' 
#        for i in self._lines_labels: i.mag_filter='nearest' 

#<Texture@Texture>:
#    on_size:
#        self.min_filter: 'nearest'
#        self.mag_filter: 'nearest'
     
""")


from biskivy.utils import utils     # Temel Araçlarımız yüklenir

bkv.utils = utils                   # Bazı araçların sorunsuz yüklenebilmesi için, bunu en son yüklüyoruz.

# from biskivy.pare.bildiri import Bildiri
# Bildiri.bilgi("Kivi", "Kivy Blender GUI yüklendi")


#import threading
#threading.Thread(target=bkv.utils.winpreferences.toggle).start()