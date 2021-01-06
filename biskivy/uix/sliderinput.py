from kivy.lang import Builder

from biskivy.uix.ortak.input import OrtakInput

Builder.load_string("""
<BisSliderInput>:
    widget_type: "kayac"
    
    # Kaydırma bar renkleri
    prop_color: []
    prop_text: ""
    prop_min: 0
    prop_max: 1
    prop_value: 1
    
    text: self.prop_text
    padding: self.height/2, 0
    
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
    
                       
    canvas:
        # Kayan RENKLİ kısım
        Color:
            rgba: (self.prop_color or bkv.prefs.input.renk_t_item) \
                if not self.aktif and self.prop_value > 0 else [0,0,0,0]
        RoundedRectangle:
            pos: self.pos
            size: (self.prop_value / self.prop_max)*self.width, self.height
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]
        
    
    canvas.after:
        Color:
            rgba: [1,1,1,0.2] if self.hovered and not self.aktif and not self.ids.ortinput.move else [0,0,0,0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]
            
        Color:
            rgba: [0, 0, 0, .2] if self.disabled else [0, 0, 0, 0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]
        
        
    
    FloatLayout:
        size_hint: None, 1
        size: 1, self.parent.height
        pos: self.parent.pos
        PropLabel:
    
    OrtakTInput:
        id: ortinput




""")


class BisSliderInput(OrtakInput):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi

    .. versionchanged:: 23.05.2020
        İsim değişikliği -> Kayaç -> SliderInput
    """
