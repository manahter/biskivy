from kivy.lang import Builder

from biskivy.uix.ortak.input import OrtakInput

Builder.load_string("""
<MiniImageButton@ButtonBehavior+Image>:
    margin: 0
    size_hint_x: None
    width: int(self.parent.height / 3 * 2)

    #pos: self.parent.pos #[0] + ((self.parent.width-self.parent.height) / 2) + self.margin/2, self.parent.pos[1] + self.margin/2

    color: [1, 1, 1, (.6 if self.parent.hovered and not self.parent.aktif and self.state=="normal" else 0)]


<BisNumberInput>:
    prop_text: ""
    text: self.prop_text
    
    canvas.before:
        Color:
            rgba: bkv.prefs.input.renk_outline
        Line:
            width: 1
            rounded_rectangle: [*self.pos, *self.size, self.sola, self.saga, self.sagu, self.solu]
        Color:
            rgba: bkv.prefs.input.renk_selected if self.aktif else bkv.prefs.input.renk_inner
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]
    
    canvas.after:
        Color:
            rgba: [0, 0, 0, .2] if self.disabled else [0, 0, 0, 0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]
            
    
    # Azalt Butonu
    MiniImageButton:
        source: bkv.paths.icons.sayac_azalt
        on_press:
            self.parent.islem("-")
    
    # Açıklama Metni
    FloatLayout:
        size_hint: None, 1
        size: 1, self.parent.height
        pos: self.parent.pos
        PropLabel:
    
    # Number
    OrtakTInput:
        canvas.after:
            Color:
                rgba: [1,1,1,0.2] if self.parent.hovered and not self.focus else [0,0,0,0]
            Rectangle:
                pos: self.pos
                size: self.size 

    # Artır Butonu
    MiniImageButton:
        source: bkv.paths.icons.sayac_artir
        on_press:
            self.parent.islem("+")
""")


class BisNumberInput(OrtakInput):
    """
    Colors
        renk_text: (.902, .902, .902, 1)
        renk_t_selected: (1, 1, 1, 1)
        renk_t_item: (.337, .502, .761, .8)

        # Dolgu renkleri
        renk_inner: (.349,.349,.349,1)
        renk_selected: (.314,.314,.314,1)
        renk_outline: (.267,.267,.267,1)

    Props
        prop_type: float
            "int" veya "float" değeri girilebilir
        prop_unit: ""
            Sayının yanında görünmesi istenen birim girilir.
            Örn şöyle görünür:  22 br
        prop_min: 0
            Sayının alabileceği minimum değer
        prop_max: 1000000
            Sayının alabileceği maximum değer
        prop_step: 0.1
            Sayının her bir adımda artış/azalır miktarı.
            Eğer sayı "float" ise otomatik olarak 0.1'dir
            Eğer sayı "int" ise otomtik olarak 1'dir.
            Değiştirebilirsiniz
        prop_value: 0
            Sayıyı tutan ana değişken
        prop_default: 0
            Sayacın sıfırlandığında, sayının alması istenen değer
            !!! Henüz bu özellik eklenmedi !!!

    disabled: False
        Sayacın kullanımı aktif/pasif yapılabilir.

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    .. versionchanged:: 23.05.2020
        İsim değişikliği -> Sayac -> BisNumberInput
    """
