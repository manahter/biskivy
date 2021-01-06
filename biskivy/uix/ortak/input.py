from kivy.uix.textinput import TextInput
from biskivy.uix.boxlayout import BisBoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

from biskivy.behaviors import HoverBehaviorS1
from biskivy.avars import AvarS1Round


Builder.load_string("""
<PropLabel@BisLabel>:
    height: int(self.font_size*1.5)

    disabled: self.parent.disabled
    pos: self.parent.x + (self.texture_size[0] / 2), self.parent.y
    text: self.parent.parent.text
    opacity: 0 if self.parent.parent.aktif else 1
    halign: "left"
    
    
<OrtakTInput>:
    pres: False    # Bastığımızda / Bıraktığımızda
    move: False    # Sürüklerken
    
    write_tab: False
    multiline: False

    size_hint_y: None
    height: int(self.font_size*1.5)

    text_width: 0       # Text'i ortalamak için
    padding: [ ( (self.width - self.text_width) / 2 if self.width-10 > self.text_width else 0) if not self.focus else 0,\
        self.height / 2.0 - (self.line_height / 2.0) * len(self._lines),\
        0,0]   
    halign: "left" if self.focus else ( "right" if self.parent.text else "auto" )
    font_size: bkv.prefs.scale.font_size

    text: self.parent.hint_text if not self.focus else str(self.parent.prop_value)
    
    hint_text_color: bkv.prefs.input.renk_text
    background_color: 0,0,0,0
    foreground_color: bkv.prefs.input.renk_text 
    selection_color: bkv.prefs.input.renk_t_item

    disabled: self.parent.disabled
    
    # Text giriş esnasında, mevcut texti geçici olarak tutar
    _last_text: ""
    
    #on_parent:
    #    # Text'in genişliğini güncelle
    #    self.text_width = self._get_text_width(self.text, self.tab_width, self._label_cached)

    on_text:
        # Text'in genişliğini güncelle
        self.text_width = self._get_text_width(self.text, self.tab_width, self._label_cached)

        # Text, kutudan daha genişse, kutunun genişliğini baz al
        if self.text_width > self.width - 10: self.text_width = self.width - 10
        
        if self.focus: self._last_text = self.text
        
    on_size:
        # Text'in genişliğini güncelle
        self.text_width = int(self._get_text_width(self.text, self.tab_width, self._label_cached))
    
    on_focus:
        # TextInputa odaklanıldığını, üste bildir
        self.parent.aktif = self.focus

        # Odak dışına çıkınca, girilen metni, prop_value'ye bildir
        if not args[1] and self._last_text: self.parent.prop_value = self._last_text
        
        # Odaklanınca, cursorun konumunu güncelle
        if args[1]: self.cursor = (0, 0)
        
<OrtakInput>:
    scale_round: bkv.prefs.input.scale_round
    size_hint_y: None
    height: self.minimum_height
    aktif: False
    text: ""
    widget_type: "sayac"
    prop_type: float
    prop_unit: ""
    prop_min: 0
    prop_max: 1000000
    prop_step: 0.1 if self.prop_type is float else 1
    prop_value: 0
    prop_default: 0
    prop_round: 6
    disabled: False
    hint_text: "{:.3f} {}".format(self.prop_value, self.prop_unit) if not self.aktif and self.prop_type is float else "{} {}".format(self.prop_value, self.prop_unit)
    
    on_prop_value:
        self.on_prop_value2(*args)
        

""")


class OrtakInput(BisBoxLayout, HoverBehaviorS1, AvarS1Round):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    def islem(self, islem="+"):
        if self.parent.disabled:
            return
        max_pointed = 0
        _volatile = str(self.prop_value)
        if "." in _volatile:
            max_pointed = len(_volatile[_volatile.index("."):])

        _volatile = str(self.prop_step)
        if "." in _volatile:
            max_pointed = max(len(_volatile[_volatile.index("."):]), max_pointed)

        o = self.prop_value + self.prop_step if islem == "+" else self.prop_value - self.prop_step
        self.prop_value = round(o, max_pointed)

    def on_prop_value2(self, *args):
        """Eğer prop_value ayarlanan değerlerde değilse, o değerlere dönüştürülür"""

        prop_value = self.prop_value

        # Eğer prop_value ayarlanan tipte değilse, o tipe dönüştür
        if not (type(prop_value) is self.prop_type):
            try:
                # Eğer gelen değer "5.8" şeklindeyse ve int'e dönüştürülmek isteniyorsa,
                # öncelikle floata dönüştürülür ki hata vermesin.
                if (self.prop_type is int) and (type(prop_value) is str) and ("." in prop_value):
                    prop_value = float(prop_value)

                prop_value = self.prop_type(prop_value)
            except:
                print("prop_value -> hata")
                return

        if self.prop_type in (float, int):
            # Belirlenen değer aralığında değilse, prop_value düzenle
            if prop_value > self.prop_max: prop_value = self.prop_max
            if prop_value < self.prop_min: prop_value = self.prop_min

            # Virgülden sonrası, belirlenen basamak sayısından büyükse, yuvarla
            yuv = round(prop_value, self.prop_round)
            if type(prop_value) is float and yuv != prop_value: prop_value = yuv

        self.prop_value = prop_value


class OrtakTInput(TextInput):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """

    def on_touch_down(self, touch):
        # TextInput yazma modundaysa işlem yapma
        if self.focus:
            return super(OrtakTInput, self).on_touch_down(touch)

        # Bu ata'a değmediyse işlem yapma
        if not self.collide_point(*touch.pos): return

        # Bu ata'a basıldı
        self.pres = True

        # Bu ata'ın basıldığı andaki konumu
        self.move_pos = touch.pos

        # Window.show_cursor = True

    def on_touch_move(self, touch):
        # TextInput yazma modundaysa işlem yapma
        if self.focus:
            return super(OrtakTInput, self).on_touch_move(touch)

        # Bu ata'a değmediyse işlem yapma
        if not self.pres:
            return

        # Hareket halinde
        self.move = True

        # Tip -> SAYAC ise, artıma ve azaltma işlemleri
        if self.parent.widget_type == "sayac":
            if touch.x - 1 > self.move_pos[0]:
                self.parent.islem("+")
                self.move_pos = touch.pos

            elif touch.x + 1 < self.move_pos[0]:
                self.parent.islem("-")
                self.move_pos = touch.pos

        # Tip -> KAYAC ise, artıma ve azaltma işlemleri
        else:
            # NOT: self.width   --> yerine -->  (self.width/2)  --> yazdık. Daha rahat kaydırılıyor.
            # PROP_TYPE -> int ise artıma ve azaltma işlemleri
            if self.parent.prop_type is int:
                # Mouse, kaç piksel kaydırıldığında, ayarlanmış (prop_step adımı) 1 adıma  denk geliyor.
                piksel_step = ((self.width/2) / (self.parent.prop_max - self.parent.prop_min)) * self.parent.prop_step

                # PIKSEL_STEP kadar artı yönde kaydırıldıysa, PROP_VALUE'i artır
                if piksel_step <= touch.x - self.move_pos[0]:
                    '''asdasdasd'''
                    self.parent.islem("+")
                    self.move_pos = touch.pos
                elif -piksel_step >= touch.x - self.move_pos[0]:
                    self.parent.islem("-")
                    self.move_pos = touch.pos

            # PROP_TYPE -> float ise artıma ve azaltma işlemleri
            else:
                self.parent.prop_value += (touch.x - self.move_pos[0]) / (self.width/2)
                self.move_pos = touch.pos

    def on_touch_up(self, touch):
        # TextInput yazma modundaysa işlem yapma
        if self.focus:
            return super(OrtakTInput, self).on_touch_up(touch)

        # Bu ata'a değmediyse işlem yapma
        if not self.pres:
            return
        # Bu widgetta kaydırma işlemi olmadıysa işlem yapma
        if not self.move:
            # TextInput'un genişliği çok küçük olduğunda,
            # Hata vermesi sebebiyle, if deyimi eklendi.
            if self.width > self.height:
                super(OrtakTInput, self).on_touch_down(touch)

        # Değerleri sıfırla
        self.pres = False
        self.move = False
