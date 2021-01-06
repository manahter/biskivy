"""
App içinden erişilebilir,
Genel Biskivy Ayarları.
"""
from kivy.properties import VariableListProperty, NumericProperty, StringProperty, DictProperty, ListProperty

from biskivy.defterdar import Defterdar


class BisScale(Defterdar):
    """Scale bilgilerini tutar"""
    def load(self):
        self.muhimme = "prefs/theme/scale.json"
        self.defter_listesi = ["size", "font", "round", "roundkats"]

    size = NumericProperty(4)
    font = NumericProperty(13)
    round = NumericProperty(.2)
    roundkats = NumericProperty(20)     # --> Kullanım dışı

    font_size = NumericProperty(13)

    def __init__(self):
        super(BisScale, self).__init__()
        self.bind(size=self.set_font_size)
        self.bind(font=self.set_font_size)
        self.set_font_size()    # Başlangıçta font_size değeri atansın diye

    def set_font_size(self, *args):
        """size ve font değerleri değişince, font_size değeri otomatik güncellenir"""
        self.font_size = int(self.size * self.font)


class BisButton(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/button.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline",
                               "scale_round"]

    # Text renkleri
    renk_text = VariableListProperty((.91, .91, .91, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((1, 1, 1, .1))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.345, .345, .345, 1))
    renk_selected = VariableListProperty((.337, .502, .761, 0.902))
    renk_outline = VariableListProperty((.216, .216, .216, 1))

    # Scale Round
    scale_round = NumericProperty(.5)


class BisLabel(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/label.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline"]

    # Text renkleri
    renk_text = VariableListProperty((.851, .851, .851, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((.243, .243, .243, 1))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.192, .192, .192, 1))
    renk_selected = VariableListProperty((.337, .502, .761, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))


class BisTextInput(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/textinput.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline",
                               "scale_round"]

    # Text renkleri
    renk_text = VariableListProperty((.902, .902, .902, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((.098, .098, .098, .8))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.122, .122, .122, 1))
    renk_selected = VariableListProperty((.314, .314, .314, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))

    # Scale Round
    scale_round = NumericProperty(.5)


class BisMenu(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/menu.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline",
                               "scale_round"]

    # Text renkleri
    renk_text = VariableListProperty((.933, .933, .933, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((.6, .6, .6, 1))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.192, .192, .192, 1))
    renk_selected = VariableListProperty((.337, .502, .761, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))

    # Scale Round
    scale_round = NumericProperty(.5)


class BisSelectMenu(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/selectmenu.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline",
                               "scale_round"]

    # Text renkleri
    renk_text = VariableListProperty((.851, .851, .851, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((.6, .6, .6, 1))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.192, .192, .192, 1))
    renk_selected = VariableListProperty((.337, .502, .761, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))

    # Scale Round
    scale_round = NumericProperty(.5)


class BisPanel(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/panel.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline"]

    # Text renkleri
    renk_text = VariableListProperty((.933, .933, .933, 1))
    renk_t_selected = VariableListProperty((1, 1, 1, 1))
    renk_t_item = VariableListProperty((.6, .6, .6, 1))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.259, .259, .259, 1))
    renk_selected = VariableListProperty((.1, .1, .1, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))


class BisInput(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/input.json"
        self.defter_listesi = ["renk_text", "renk_t_selected", "renk_t_item",
                               "renk_inner", "renk_selected", "renk_outline",
                               "scale_round"]

    # Text renkleri
    renk_text = VariableListProperty((.902, .902, .902, 1))
    renk_t_selected = VariableListProperty((.5, .5, .5, .2))
    renk_t_item = VariableListProperty((.337, .502, .761, .8))

    # Dolgu renkleri
    renk_inner = VariableListProperty((.349, .349, .349, 1))
    renk_selected = VariableListProperty((.314, .314, .314, 1))
    renk_outline = VariableListProperty((.267, .267, .267, 1))

    # Scale Round
    scale_round = NumericProperty(.5)


class BisColor(Defterdar):
    def load(self):
        self.muhimme = "prefs/theme/color.json"
        self.defter_listesi = ["scale_round"]

    # Scale Round
    scale_round = NumericProperty(.5)


class BisPaths(Defterdar):
    def load(self):
        self.muhimme = "prefs/paths.json"
        self.defter_listesi = ["icons"]

    icons = StringProperty()
    """Path to icons directory."""


class __Empty:
    pass


prefs = __Empty()
prefs.scale = BisScale()
prefs.label = BisLabel()
prefs.button = BisButton()
prefs.input = BisInput()
prefs.textinput = BisTextInput()
prefs.color = BisColor()
prefs.menu = BisMenu()
prefs.selectmenu = BisSelectMenu()
prefs.panel = BisPanel()

prefs.paths = BisPaths()
#app.prefs.paths.images = os.path.join(path, f"images{os.sep}")
"""Path to images directory."""

