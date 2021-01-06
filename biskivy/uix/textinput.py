from kivy.lang import Builder

from biskivy.uix.boxlayout import BisBoxLayout
from biskivy.behaviors import HoverBehaviorS1
from biskivy.avars import AvarS1Round

Builder.load_string("""
<BisTextInput>:
    
    scale_round: bkv.prefs.textinput.scale_round
    prop_text: ""
    
    # İçine girilip girilmediğini gösterir. Only read
    aktif: False
    
    size_hint_y: None
    height: self.minimum_height
    
    canvas.before:
        Color:
            rgba: bkv.prefs.textinput.renk_outline
        Line:
            width: 1
            rounded_rectangle: [*self.pos, *self.size, self.sola, self.saga, self.sagu, self.solu]
        Color:
            rgba: bkv.prefs.textinput.renk_selected if self.aktif else bkv.prefs.textinput.renk_inner
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]

    canvas.after:
        Color:
            rgba: [1,1,1,0.02] if self.hovered else [0,0,0,0]
        RoundedRectangle:
            pos: self.pos
            size: self.size 
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.parent else [0,]

    TextInput:
        write_tab: False
        multiline: False
        
        font_size: bkv.prefs.scale.font_size

        padding: [self.height/2, self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), self.height / 2, 0]
        size_hint_y: None
        height: int(self.font_size*1.5)
        
        hint_text: "Metin Giriniz"
        hint_text_color: bkv.prefs.textinput.renk_selected
        background_color: 0,0,0,0
        foreground_color: bkv.prefs.textinput.renk_text
        selection_color: bkv.prefs.textinput.renk_t_item
        
        disabled: self.parent.disabled
        
        text: self.parent.prop_text
        #halign: self.parent.halign
        
        on_text:
            self.parent.prop_text = self.text
            self.cursor = (len(self.text), 0)
        on_focus:
            self.parent.aktif = self.focus

""")


class BisTextInput(BisBoxLayout, HoverBehaviorS1, AvarS1Round):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi

    .. versionchanged:: 23.05.2020
        halign iptal edildi
        Cursor sona alma problemi düzeltildi.
    """
