from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

from biskivy.behaviors import HoverBehaviorS1
from biskivy.avars import AvarS1Round
from biskivy.uix.ortak.wiarc import WiARC
from biskivy.uix.window import BisWindow

"""
Kod Yapısı;
    BisMenu:
        MenyuPen:
            BisMenuItem:
                BisMenuKapak:
                    Image:
                    BisLabelAligned:
                    Image:
                BisMenuKasa:
                    BisMenuItem:
                    BisMenuItem:
                    BisMenuItem:
                    BisMenuItem:
                    BisMenuItem:
                    BisMenuItem:

Kullanım:
    BisMenu:
        BisMenuItem:
            title: "Başlık"
            SomeLayout
        BisMenuItem:
            SomeWidget
            SomeWidget
        BisMenuItem:
            ...
        BisMenuItem:
"""


Builder.load_string("""
#:import random random.uniform
<BisMenuKapak>:
    size_hint_y: None
    
    on_press:
        self.parent.collapse = not self.parent.collapse
        
    canvas.before:
        Color:
            rgba: bkv.prefs.menu.renk_selected if self.hovered or not self.parent.collapse else [0, 0, 0, 0]
        Rectangle:
            pos: self.pos
            size: self.size
            
    ### Icon
    Image:    
        size_hint_x: None if self.parent.size_hint_x > 0 else 1
        size_hint_y: None if self.parent.size_hint_x > 0 else 1

        width: self.parent.height
        height: self.parent.height
        pos: self.parent.pos
        
        source: self.parent.parent.prop_icon or bkv.paths.icons.mv
        color: bkv.prefs.menu.renk_t_item


    ### LABEL
    BisLabelAligned:
        text: self.parent.parent.prop_text
        size_hint_x: None if self.parent.width > 5 else 1
        
        # Size
        width: self.texture_size[0]
        
        # Text özellikleri
        halign: "left"        # Yatay Ortala

        # Renk
        color: bkv.prefs.menu.renk_text
        
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.texture_size[1] + dp(3)
        
        
    ### LABEL
    BisLabelAligned:
        text: self.parent.parent.prop_hint or " "
        color: bkv.prefs.menu.renk_t_item
        size_hint_x: self.texture_size[0]
        
        # Size
        width: self.texture_size[0] + dp(40)
                
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.texture_size[1] + dp(3)
        
    ### Mnüyü Genişlet Butonu
    Image:    
        size_hint: None, None
        width: self.parent.height / 2
        height: self.parent.height
        pos: self.parent.pos
        
        source: bkv.paths.icons.menyu_closed if self.parent.parent.collapse else bkv.paths.icons.menyu_opened
        color: bkv.prefs.menu.renk_t_item if self.parent.parent.sub_item else [0,0,0,0]
    
            
<BisMenuKasa>:
    orientation: self.parent.prop_orientation or 'horizontal'
    spacing: self.parent.prop_spacing
    padding: [0,0,0,0] if self.parent.collapse else self.parent.prop_padding
    opacity: 0 if self.parent.collapse else 1
    
    # Size
    size_hint_x: None if self.parent.collapse else 1
    size_hint_y: None
    width: 1 if self.parent.collapse else self.minimum_height
    height: 0 if self.parent.collapse else self.minimum_height
    
    # Show/Hide
    disabled: True if self.parent.collapse else False
    on_parent: 
        self.opacity = 0 if self.parent.collapse else 1
        
    canvas.before:
        Color:
            rgba: (.1, .1, .1, .768) if self.parent._drn % 2  == 1 else (.15, .15, .15, .768)
        Rectangle:
            pos: self.pos
            size: self.size
    
    
<BisMenuItem>:    
    ############################## Kontrol Edilebilir Degiskenler1    
    # Çerçeve Başlık Metni
    prop_text: "Title"
    prop_hint: ""
    prop_bind: None
    prop_orientation: "vertical"
    prop_padding: [10,1,0,0]
    prop_spacing: 1
    
    # Çerçeve Başlık iconu
    prop_icon: ""                
    
    # 0.1'de güzel. Animasyon hızı
    anim_duration: 0    # 0.1 'de fena değil
    ##############################################################
    
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height
   
            
    BisMenuKapak:
    BisMenuKasa:


<BisMenuSeperator>:
    size_hint_y: None
    height: 1
    canvas:
        Color:
            rgba: 1,1,1,.1
        Rectangle:
            pos: self.pos
            size: self.size


<BisMenu>:
    
    ################### Burayı dekarte et
    scale_round: bkv.prefs.menu.scale_round
    background_color: 0,0,0,0       # ArkaPlan resmini kaldırır
    size_hint_y: None
    
    ###################################


    # text veya prop_text girilebilir.
    prop_text: " "  
    text: self.prop_text
    
    font_size: bkv.prefs.scale.font_size
    
    # Menü, Butonun ne tarafında açılsın -> auto, bottom, top, left, right
    # Burası kesin yönünü belirtmez. Sadece önceliği belirtir.
    prop_align: "auto"     
    
    # Açılan Menü Penceresinin genişliği
    prop_width: 260
    on_prop_width:
        self.biswindow.prop_width = self.prop_width
    
    ################## Bunları dekarte et
    sisme: 4 if self.tek else 0     # Butona basınca, kaç piksel kabaracak (highlight gibi..)
    
    color: bkv.prefs.menu.renk_t_selected if self.hovered else bkv.prefs.menu.renk_text
    
    # Size
    gen: self.texture_size[0] + dp(40)
    height: self.texture_size[1] + dp(4)
    width: self.gen if self.yat else self.parent.width
    
    # Text özellikleri
    halign: "center"        # Yatay Ortala
    valign: "center"        # Dikey Ortala
    shorten: True           # Küçüldükçe, yazıyı "Xx...xx" gibi kısalt
    text_size: ((None if not self.size_hint_x else self.width) , None)      # Bu şekilde daha doğru. Sakın kısaltma bunu
    #######################################
    
    on_press:
        self.biswindow.toggle()
        
    canvas.before:
        Color:
            rgba: bkv.prefs.menu.renk_outline
        Line:
            width: 1
            rounded_rectangle: [*self.pos, *self.size, self.sola, self.saga, self.sagu, self.solu]
        Color:
            rgba: bkv.prefs.menu.renk_selected if self.hovered or self.biswindow.opened else bkv.prefs.menu.renk_inner
        RoundedRectangle:
            pos: self.pos if self.state=='normal' else [self.pos[0]-self.sisme/2, self.pos[1]-self.sisme/2]
            size: self.size if self.state=='normal' else [self.size[0]+self.sisme, self.size[1]+self.sisme]
            radius: [self.solu, self.sagu, self.saga, self.sola] if self.gen else [0,]
""")


class BisMenu(WiARC, HoverBehaviorS1, Button, AvarS1Round):
    """Açılır Menü. Alt öğelerden birisi tıklandığında,
    prop_bind çalışır. Ayarlanan işlem yürütülür.

    .. versionchanged:: 22.05.2020
        Verisyon takip tarihi eklendi
    """

    def __init__(self, **kwargs):
        self.biswindow = BisWindow()        # Çocuk -> AçılırPen
        self.biswindow.prop_spacing = 0
        self.biswindow.prop_padding = 0, 0, 0, 0
        self.biswindow.prop_width = 400
        self.biswindow.ata = self       # AçılırPen'in atası benim

        self.wiarc_accepted_widgets = (BisMenuItem, BisMenuSeperator)
        self.wiarc_accepted_to_kasa = True
        self.wiarc_widget_kasa = self.biswindow
        super(BisMenu, self).__init__(**kwargs)


class BisMenuItem(BoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """

    sub_item = BooleanProperty(False)
    """Alt öğe var mı"""

    collapse = BooleanProperty(True)
    kasa = None
    kapak = None
    prop_bind = None
    #_pen = None

    _drn = 0
    """Derinlik -> Kaçıncı kuşak biswindow
    Bununla, iç içe item'lerin arkaplanı bir koyu, bir açık şeklinde sıralanır"""

    ###################################################
    def add_widget(self, widget, index=0, canvas=None):
        # Eklenen Widget Kasa ise
        if isinstance(widget, BisMenuKasa):
            super(BisMenuItem, self).add_widget(widget, index, canvas)
            self.kasa = widget
            return

        # Eklenen Widget Kapak ise
        if isinstance(widget, BisMenuKapak):
            super(BisMenuItem, self).add_widget(widget, 1, canvas)
            self.kapak = widget
            return

        # Eklenen Widget hiçbiri değilse, Kasaya koy
        #widget._pen = self._pen
        widget._drn = self._drn + 1
        self.kasa.add_widget(widget, index, canvas)
        self.sub_item = len(self.kasa.children) > 0

    def remove_widget(self, widget):
        self.kasa.remove_widget(widget)
        self.sub_item = len(self.kasa.children) > 0

    def clear_widgets(self, children=None):
        self.kasa.clear_widgets(children=children)
        self.sub_item = len(self.kasa.children) > 0
    ###################################################

    def on_collapse(self, *args):
        """Animasyonlu, açılır/kapanır"""

        # self'e tıklandıysa, ve işlem tanımlanmışsa -> işlemi yap
        if self.collapse and self.prop_bind:
            #self._pen.close()
            self.prop_bind()

        # Alt öğeler yoksa, işlemi yapıp self'i kapat
        if not self.sub_item:
            self.collapse = True
            return

        # Bu açıldıysa, diğer kardeş Item'leri kapat
        for i in self.parent.children:
            if not isinstance(i, BisMenuItem):
                continue
            if i.kasa.opacity != 0:
                i.collapse = True


class BisMenuKapak(HoverBehaviorS1, ButtonBehavior, BoxLayout):
    """Item'ın kapağı, Icon-Text-Hotkey-CollapseIcon
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """


class BisMenuKasa(BoxLayout):
    """Item içeriğinin eklendiği alan
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """


class BisMenuSeperator(BoxLayout):
    """Itemler arası ince bir ayraç
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
