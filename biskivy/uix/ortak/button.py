from kivy.lang import Builder

from biskivy.behaviors import HoverBehaviorS1
from biskivy.avars import AvarS1Round

Builder.load_string("""
<OrtakButton>:
    ################# Burayı dekarte et
    scale_round: bkv.prefs.button.scale_round
    background_color: 0,0,0,0       # ArkaPlan resmini kaldırır
    size_hint_y: None    
    
    sisme: 4 if self.tek else 0     # Butona basınca, kaç piksel kabaracak (highlight gibi..)
    
    font_size: bkv.prefs.scale.font_size
    color: bkv.prefs.button.renk_t_selected if self.hovered else bkv.prefs.button.renk_text
    
    # Size
    gen: self.texture_size[0] + dp(40)
    height: self.texture_size[1] + dp(4)
    width: self.gen if self.yat or not self.parent else self.parent.width
    
    #opacity: 0 if self.width < 1 or self.height < 1 else 1
    
    # Text özellikleri
    halign: "center"        # Yatay Ortala
    valign: "center"        # Dikey Ortala
    shorten: True           # Küçüldükçe, yazıyı "Xx...xx" gibi kısalt
    text_size: ((None if not self.size_hint_x else self.width) , None)      # Bu şekilde daha doğru. Sakın kısaltma bunu
    
    ###########################################
    
    
    prop_icon: ""           # Buton prop_icon'u girilebilir
    prop_only_icon: False
    
    prop_text: " "
    on_prop_text: if not self.prop_text: self.prop_text = " "
    
    text: self.prop_text    # Buton metini girilebilir
    
    # Only Icon'un doğru çalışabilmesi için;
    on_size:
        self.size_hint_x = None if self.prop_only_icon else 1
        if self.prop_only_icon: self.width = self.height
    
        
    canvas.before:
        Color:
            rgba: bkv.prefs.button.renk_outline
        Line:
            width: 1
            rounded_rectangle: [*self.pos, *self.size, self.sola, self.saga, self.sagu, self.solu]
        Color:
            rgba: bkv.prefs.button.renk_selected if self.state=='down' else bkv.prefs.button.renk_inner
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.gen else [0,]

    canvas.after:
        Color:
            rgba: bkv.prefs.button.renk_t_item if self.hovered else [0,0,0,0]
        RoundedRectangle:
            pos: self.pos
            size: self.size 
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.gen else [0,]

    Image:
        margin: 0
        size_hint: None, 1
        boy: self.parent.height
        pos: (self.parent.pos[0] + ((self.parent.width-self.parent.height) / 2) + self.margin/2,\
              self.parent.pos[1] + self.margin/2) if self.parent.text == " " else self.parent.pos
        width: self.boy
        height: self.boy
        source: self.parent.prop_icon
        color: bkv.prefs.button.renk_text if self.parent.width > self.width/2 and self.texture else [0,0,0,0]

        #mipmap: True   # AntiAliasing
        #on_texture:
        #    if self.texture: self.texture.min_filter='nearest'
        #    if self.texture: self.texture.mag_filter='nearest'
""")


class OrtakButton(HoverBehaviorS1, AvarS1Round):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
