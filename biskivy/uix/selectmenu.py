from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from biskivy.behaviors import HoverBehaviorS1
from biskivy.avars import AvarS1Round
from biskivy.uix.ortak.wiarc import WiARC
from biskivy.uix.window import BisWindow

"""
Kod Yapısı;
    BisSelectMenu:
        MenyuPen:
            BisSelectMenuItem:
            BisSelectMenuItem:
            BisSelectMenuItem:
            BisSelectMenuItem:
            BisSelectMenuItem:
            BisSelectMenuItem:
                Image:
                BisLabelAligned:
                Image:

Kullanım:
    BisSelectMenu:
        BisSelectMenuItem:
            title: "Başlık"
            SomeLayout
        BisSelectMenuItem:
            SomeWidget
            SomeWidget
        BisSelectMenuItem:
            ...
        BisSelectMenuItem:
"""

Builder.load_string("""
<BisSelectMenuItem>:
    
    # Bu pencereyi açan widget oluyor genelde
    control_parent: None
    
    ############################ Kontrol Edilebilir Degiskenler
    #############################################################      

    # Item Metni
    prop_text: "Title"
    
    # Item Ipucu
    prop_hint: ""

    # Item Iconu
    prop_icon: ""
    
    # Item Bind Func
    prop_bind: None
    
    ##############################################################

    size_hint_y: None
    
    on_state:
        if self.state == "down": self.control_parent.selected_item = self
        if self.state == "down" and self.prop_bind: self.prop_bind(*args) 
        
    canvas.before:
        Color:
            rgba: bkv.prefs.selectmenu.renk_selected if self.hovered or self.state == "down" else [0, 0, 0, 0]
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: (1, 1, 1, .2) if self.state == "down" else [0, 0, 0, 0]
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

        source: self.parent.prop_icon or bkv.paths.icons.mv
        color: bkv.prefs.selectmenu.renk_text


    ### LABEL
    BisLabelAligned:
        text: self.parent.prop_text
        size_hint_x: None if self.parent.width > 5 else 1
        
        # Size
        width: self.texture_size[0]
        
        # Text özellikleri
        halign: "left"        # Yatay Ortala
        
        # Renk
        color: bkv.prefs.selectmenu.renk_text
        
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.texture_size[1] + dp(3)


    ### LABEL -> Hint
    BisLabelAligned:
        text: self.parent.prop_hint or " "
        color: bkv.prefs.selectmenu.renk_t_item
        size_hint_x: self.texture_size[0]

        # Size
        width: self.texture_size[0] + dp(40)

        # Text özellikleri
        halign: "right"        # Yatay Ortala
        
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.texture_size[1] + dp(3)


<BisMenuSeperator>:
    size_hint_y: None
    height: 1
    canvas:
        Color:
            rgba: 1,1,1,.1
        Rectangle:
            pos: self.pos
            size: self.size


<BisSelectMenu>:
    scale_round: bkv.prefs.selectmenu.scale_round

    size_hint: 1, None
    height: self.minimum_height
        
    # PROPS
    prop_title: ""
    on_prop_title: self.biswindow.prop_title = self.prop_title
    prop_items: []
    on_prop_items: self.create_items()
    selected_item: None
    
    # Menü, Butonun ne tarafında açılsın -> auto, bottom, top, left, right
    # Burası kesin yönünü belirtmez. Sadece önceliği belirtir.
    prop_align: "auto"     

    # Açılan Menü Penceresinin genişliği
    prop_width: 260
    on_prop_width:
        self.biswindow.prop_width = self.prop_width

    on_press:
        self.biswindow.toggle()

    canvas.before:
        Color:
            rgba: bkv.prefs.selectmenu.renk_outline
        Line:
            width: 1
            rounded_rectangle: [*self.pos, *self.size, self.sola, self.saga, self.sagu, self.solu]
        Color:
            rgba: (1, 1, 1, .1) if self.hovered or self.biswindow.opened else bkv.prefs.selectmenu.renk_inner
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [self.solu, self.sagu, self.saga, self.sola]
                
    ### Icon
    Image:    
        size_hint_x: None if self.parent.size_hint_x > 0 else 1
        size_hint_y: None if self.parent.size_hint_x > 0 else 1

        width: self.parent.height
        height: self.parent.height
        pos: self.parent.pos
        
        source: (self.parent.selected_item.prop_icon if self.parent.selected_item else 0) or bkv.paths.icons.mv
        color: (1, 1, 1, 1) if self.parent.hovered else bkv.prefs.selectmenu.renk_text


    ### LABEL
    BisLabelAligned:
        text: self.parent.selected_item.prop_text if self.parent.selected_item else " "
        
        # Text özellikleri
        halign: "left"        # Yatay Ortala
        
        # Renk
        color: (1, 1, 1, 1) if self.parent.hovered else bkv.prefs.selectmenu.renk_text
        
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.texture_size[1] + dp(3)
        
                
    ### Mnüyü Genişlet Butonu
    Image:    
        size_hint: None, None
        width: self.parent.height
        height: self.parent.height
        pos: self.parent.right - self.width, self.parent.y 
        
        color: bkv.prefs.selectmenu.renk_text
        source: bkv.paths.icons.selectmenu
""")


class BisSelectMenu(WiARC, HoverBehaviorS1, ButtonBehavior, BoxLayout, AvarS1Round):
    """Açılır Menü. Alt öğelerden birisi tıklandığında,
    bind çalışır. Ayarlanan işlem yürütülür.

    .. versionchanged:: 31.05.2020
        Oluşturuldu
    """

    biswindow = None

    def __init__(self, **kwargs):
        self.biswindow = BisWindow()  # Çocuk -> AçılırPen
        self.biswindow.prop_spacing = 0
        self.biswindow.prop_padding = 0, 0, 0, 0
        self.biswindow.ata = self  # AçılırPen'in atası benim

        self.wiarc_accepted_widgets = (BisSelectMenuItem, BisMenuSeperator)
        self.wiarc_accepted_to_kasa = True
        self.wiarc_widget_kasa = self.biswindow
        super(BisSelectMenu, self).__init__(**kwargs)

    def create_items(self):
        """Menü içindeki öğeler oluşturulur"""
        self.biswindow.clear_widgets()
        secili_var_mi = False
        h = None

        # Öğeleri oluştur
        for i in self.prop_items:
            o = BisSelectMenuItem()
            o.group = str(self.prop_items)
            o.allow_no_selection = False
            o.control_parent = self
            o.prop_text = i.get("prop_text", "")
            o.prop_hint = i.get("prop_hint", "")
            o.prop_icon = i.get("prop_icon", "")
            o.prop_bind = i.get("prop_bind", None)
            o.state = "down" if i.get("prop_select", False) is True else "normal"
            h = o
            if not secili_var_mi:
                secili_var_mi = i.get("prop_select", False)
            self.biswindow.add_widget(o)

        # Eğer listede seçili öğe yoksa, EN baştaki öğeyi seç
        if not secili_var_mi and h and len(h.parent.children):
            h.parent.children[-1].state = "down"


class BisSelectMenuItem(HoverBehaviorS1, ToggleButtonBehavior, BoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """


class BisMenuSeperator(BoxLayout):
    """Itemler arası ince bir ayraç
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
