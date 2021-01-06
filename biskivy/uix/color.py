from kivy.uix.modalview import ModalView
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics import Color
from kivy.utils import get_hex_from_color, get_color_from_hex, get_random_color

#import pyscreenshot as ImageGrab
import math

from biskivy.avars import AvarS1Round
from biskivy.uix.window import BisWindow


Builder.load_string("""
#:import Window kivy.core.window.Window
#:import Image kivy.uix.image.Image
<BisColor>:
    scale_round: bkv.prefs.color.scale_round
    background_color: 0,0,0,0       # ArkaPlan resmini kaldırır
    size_hint: 1, None
    
    prop_title: ""
    on_prop_title:
        self.biswindow.prop_title = self.prop_title
    
    # Get Renkler
    get_hex: self.biswindow.hex
    get_hsv: self.biswindow.h, self.biswindow.s, self.biswindow.v
    get_rgb: self.biswindow.r, self.biswindow.g, self.biswindow.b
    get_rgba: self.biswindow.r, self.biswindow.g, self.biswindow.b, self.biswindow.a
    
    # Set Renkler
    hex: "#11001100"
    hsv: 1, 1, 1
    rgb: 1, 1, 1
    rgba:1, 1, 1, 1
    
    on_hex:
        self.on_hex2(*args)
    on_hsv:
        self.on_hsv2(*args)
    on_rgb:
        self.on_rgb2(*args)
    on_rgba:
        self.on_rgba2(*args)
        
    #on_hex:
    #    self.biswindow.renk_hex(args[1])
    #on_hsv:
    #    self.biswindow.ronk.hsv = args[1]
    #    self.biswindow.renk_guncelle()
    #on_rgb:
    #    self.biswindow.ronk.rgb = args[1]
    #    self.biswindow.renk_guncelle()
    #on_rgba:
    #    self.biswindow.ronk.rgba = args[1]
    #    self.biswindow.renk_guncelle()
    
    
    font_size: bkv.prefs.scale.font_size
    color: 1,0,0,0              # Yazı Rengi
    background_color: 1,0,0,0   # ArkaPlan iptal

    # Size
    gen: self.texture_size[0] + dp(40)
    height: self.texture_size[1] + dp(4)
    width: self.gen if self.yat else self.parent.width

    text: " "

    # Basıldığında, Renk Seçim Panelini aç
    on_press:
        self.biswindow.toggle()

    # RENK Transparan kısım için, tekrarlı grid arkaplan oluşturulur
    tekrar: None
    on_parent:
        self.tekrar = Image(source=bkv.paths.icons.trans).texture
        self.tekrar.wrap = 'repeat'
        self.tekrar.uvsize = (30, 10)

    canvas:
        # RENK -> Dolgun Kısım
        Color:
            rgb: [ self.biswindow.r, self.biswindow.g, self.biswindow.b]
        RoundedRectangle:
            pos: self.pos
            size: self.width / 2, self.height
            radius: [self.solu, 0, 0, self.sola] if self.gen else [0,]


        #######################################
        ### ARKA -> Transparan Kısmın Arkasındaki resim
        StencilPush
        RoundedRectangle:
            pos: self.x + self.width / 2, self.y
            size: self.width / 2, self.height
            radius: [0, self.sagu, self.saga, 0] if self.gen else [0,]
        StencilUse
        Color:
            rgba: [1,1,1,1]
        Rectangle:
            #pos: self.width / 2, self.y #root.parent.parent.parent.pos #self.x + self.width / 2, self.y
            pos: self.x + self.width / 2, self.y #root.parent.parent.parent.pos #self.x + self.width / 2, self.y
            texture: self.tekrar
            size: 1500, 500
        StencilUnUse
        RoundedRectangle:
            pos: self.x + self.width / 2, self.y
            size: self.width / 2, self.height
            radius: [0, self.sagu, self.saga, 0] if self.gen else [0,]
        StencilPop
        #######################################

        # RENK -> Transparan Kısım
        Color:
            rgba: [ self.biswindow.r, self.biswindow.g, self.biswindow.b, self.biswindow.a ]
        RoundedRectangle:
            pos: self.x + self.width / 2, self.y
            size: self.width / 2, self.height
            radius: [0, self.sagu, self.saga, 0] if self.gen else [0,]



<BisColorWindow>:
    id: renksecpen
    
    size_hint: None, None
    width: renk_tipi.height * 11
    
    on_width:
        if self.width > 1100: self.width = 1100
    
    # Dairesel Skalanın üzeerindeki nokta
    nokta:[50,50]
    
    hex: "#12345678"
    r: 0
    g: 0
    b: 0
    a: 0
    h: 0
    s: 0
    v: 0
    
    renk: {"r": .8, "g": .8, "b": .8, "a": .7, "h":0, "s":0, "v": 1}
        
    on_renk:
        self.renk_guncelle(eden="renk")

    # Renk Skalalarının olduğu kısım
    BisBoxLayout:
        #spacing: 40
        size_hint_y: None
        height: self.minimum_height
        padding: 0, 10, 0, 0
        WiDrag:
            id: skala
            size_hint: 8, None
            height: self.width
            source:  bkv.paths.icons.renk
            
            # Skalada rengi gösteren noktanın Koordinatı -> x,y
            nokta: self.center_x - 3 - (renksecpen.nokta[0] * (self.width/2)), \
                   self.center_y - 3 - (renksecpen.nokta[1] * (self.height/2))
            
            # Skalada işlem yapıldıkça renk_skala fonksiyonu işletilecek
            dragging_func: (renksecpen.renk_skala, self.center, self.width)
            
            #opacity: renksecpen.a
            
            # HSV'deki V değeri kadarınca görüntüyü karartır
            canvas.after:
    
                # Koyuluk ( Skalanın üzerinde perde )
                Color:
                    rgba: 0, 0, 0, (1 - renksecpen.v) #renk_v_slid.value
                RoundedRectangle:
                    pos: self.x - 2, self.y - 2
                    size: self.width + 4, self.height + 4
                    radius: [(self.width+4)/2,]
    
                # Skalada rengi gösteren nokta
                Color:
                    rgb: 1,1,1,1
                Ellipse:
                    pos: self.nokta if self.nokta else self.pos
                    size: 6,6
    
                # Skalada rengi gösteren noktanın kenarı
                Color:
                    rgba: 0,0,0,1
                Line:
                    width: 1
                    ellipse: [*(self.nokta if self.nokta else self.pos), 6, 6]
    
    
        WiDrag:
            id: renk_v_slid
    
            size_hint: 1, None
            height: skala.height
    
            source:  bkv.paths.icons.sb_dik
    
            value: 0
            on_value:
                renksecpen.r = round(self.value, 6)
                renksecpen.renk_guncelle()
    
            # Skalada rengi gösteren noktanın Koordinatı -> x,y
            nokta: self.center_x - 3, self.y - 3 + renksecpen.v * self.height
    
            # Skalada işlem yapıldıkça renk_skala fonksiyonu işletilecek
            dragging_func: (renksecpen.renk_sb, self.pos, self.size)
            
            # HSV'deki V değeri kadarınca görüntüyü karartır
            canvas.after:
    
                # Skalada rengi gösteren nokta
                Color:
                    rgb: 1,1,1,1
                Ellipse:
                    pos: self.nokta if self.nokta else self.pos
                    size: 6,6
    
                # Skalada rengi gösteren noktanın kenarı
                Color:
                    rgba: 0,0,0,1
                Line:
                    width: 1
                    ellipse: [*(self.nokta if self.nokta else self.pos), 6, 6]
    
    
    BisCombinLayout:
        #size_hint_y: 1
        id: renk_tipi
        sekme: "RGB"
        BisToggleButton:
            group: "renk_tipi"
            prop_text: "RGB"
            state: "down"
            on_state: if self.state == "down": self.parent.sekme = self.text
        BisToggleButton:
            group: "renk_tipi"
            prop_text: "HSV"
            on_state: if self.state == "down": self.parent.sekme = self.text
        BisToggleButton:
            group: "renk_tipi"
            prop_text: "Hex"
            on_state: if self.state == "down": self.parent.sekme = self.text
    
    BisBoxLayout:
        size_hint: 1, None
        height: self.minimum_height
        #size_hint_y: 4
        spacing: 10
        BisBoxLayout:
            orientation: "vertical"
            spacing: 4
    
            size_hint: 1, None
            height: self.minimum_height
            FloatLayout:
                size_hint: 1, None
                height: rgb_panel.height
    
                ############# RGB
                BisCombinLayout:
                    id: rgb_panel
                    orientation: "vertical"
                    pos: self.parent.pos if renk_tipi.sekme == "RGB" else [-self.width, -self.height]
    
                    # Sekme RGB Seçiliyse
                    opacity: 1 if renk_tipi.sekme == "RGB" else 0
                    disabled: renk_tipi.sekme != "RGB"
                    BisSliderInput:
                        id: renk_r
                        prop_text: "R"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.r
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.r = self.prop_value
                            renksecpen.renk_guncelle()
                        #renk_t_item: self.prop_value, 0, 0, 1
                    BisSliderInput:
                        id: renk_g
                        prop_text: "G"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.g
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.g = self.prop_value
                            renksecpen.renk_guncelle()
                        #renk_t_item: 0, self.prop_value, 0, 1
                    BisSliderInput:
                        id: renk_b
                        prop_text: "B"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.b
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.b = self.prop_value
                            renksecpen.renk_guncelle()
                        #renk_t_item: 0, 0, self.prop_value, 1
    
                ############# HSV
                BisCombinLayout:
                    orientation: "vertical"
                    pos: self.parent.pos if renk_tipi.sekme == "HSV" else [-self.width, -self.height]
    
                    # Sekme RGB Seçiliyse
                    opacity: 1 if renk_tipi.sekme == "HSV" else 0
                    disabled: renk_tipi.sekme != "HSV"
                    BisSliderInput:
                        id: renk_h
                        prop_text: "H"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.h
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.h = self.prop_value
                            renksecpen.renk_guncelle()
                    BisSliderInput:
                        id: renk_s
                        prop_text: "S"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.s
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.s = self.prop_value
                            renksecpen.renk_guncelle()
                    BisSliderInput:
                        id: renk_v
                        prop_text: "V"
                        prop_type: float
                        prop_max: 1
                        prop_step: 0.1
                        prop_value: renksecpen.ronk.v
                        prop_round: 6
                        on_prop_value: 
                            renksecpen.ronk.v = self.prop_value
                            renksecpen.renk_guncelle()
                
                BisBoxLayout:
                    orientation: "vertical"
                    pos: self.parent.pos if renk_tipi.sekme == "Hex" else [-self.width, -self.height]
                    size_hint: 1, 1
                    
                    # Sekme Hex Seçiliyse
                    opacity: 1 if renk_tipi.sekme == "Hex" else 0
                    disabled: renk_tipi.sekme != "Hex"
                    BisTextInput:
                        id: renk_hex
                        halign: "center"
                        on_aktif:
                            if not self.aktif: renksecpen.renk_hex(self.prop_text)
                        
                    BisLabelAligned:
                        prop_text: "(Approximate Value)"
                        size_hint_y: 1
                        halign: "center"
                        renk_text: (.7, .7, .7, .8)
                    BisLabelAligned:
                        prop_text: ""
                        size_hint_y: 1
                    
            BisBoxLayout:
                #size_hint_y: 1
                size_hint_y: None
                height: self.minimum_height
                BisSliderInput:
                    id: renk_a
                    prop_text: "A"
                    prop_type: float
                    prop_max: 1
                    prop_step: 0.1
                    prop_value: renksecpen.ronk.a
                    on_prop_value: 
                        renksecpen.ronk.a = round(self.prop_value, 6)
                        renksecpen.renk_guncelle()
                    on_parent:
                        # Bunun sayesinde, ana ronk kutucuğu da güncelleniyor..
                        renksecpen.renk_guncelle()
    
        BisCombinLayout:
            orientation: "vertical"
            size_hint_x: None
            size_hint_y: 1
            width: self.minimum_width
            BisButton:
                size_hint_x: None
                width: self.height
                prop_icon: bkv.paths.icons.damlalik
                prop_only_icon: True
                on_press:
                    renksecpen.ata.damlalik.ata = renksecpen
                    renksecpen.ata.damlalik.open()
            BisBoxLayout:
                size_hint_y: 1
                renk_outline: (.216,.216,.216,1)
                canvas:
                    Color:
                        rgba: self.renk_outline
                    Line:
                        width: 1
                        rectangle: [*self.pos, *self.size]
                        
                    #######################################
                    ### ARKA -> Transparan Kısmın Arkasındaki resim
                    StencilPush
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        
                    StencilUse
                    Color:
                        rgba: [1,1,1,1]
                    Rectangle:
                        pos: self.pos
                        texture: renksecpen.ata.tekrar if renksecpen.ata else None
                        size: 1500, 500
                    StencilUnUse
                    Rectangle:
                        pos: self.pos
                        size: self.size
                    StencilPop
                    #######################################
            
                    # RENK -> Transparan Kısım
                    Color:
                        rgba: renk_r.prop_value, renk_g.prop_value, renk_b.prop_value, renk_a.prop_value
                    Rectangle:
                        pos: self.pos
                        size: self.size

                    
            BisButton:
                width: self.height
                prop_icon: bkv.paths.icons.random_renk
                prop_only_icon: True
                on_press:
                    renksecpen.renk_random()
    
<BisColorPicker>:
    background: bkv.paths.icons.mv
    background_color: 1,1,0,0
    size_hint: None, None
    size: 0,0
""")


class BisColor(Button, AvarS1Round):
    """
    biswindow
        BisColorWindow() sınıfını tutar. (ModalView)
        Bu sınıf, Renk değiştirme ve seçme penceresini oluşturur
    damlalik
        BisColorPicker() sınıfını tutar.
        Bu sınıf, Pencere içinden bir pikselin rengini okumayı sağlar

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    biswindow = None
    damlalik = None

    def __init__(self, **kwargs):
        self.biswindow = BisColorWindow()
        self.biswindow.ata = self
        self.damlalik = BisColorPicker()
        super(BisColor, self).__init__(**kwargs)

    def on_hex2(self, *args):
        # Gelen değerler ile varolan değerler zaten aynıysa işlem yapma
        if self.get_hex != args[1]:
            self.biswindow.renk_hex(args[1])

    def on_hsv2(self, *args):
        # Gelen değerler ile varolan değerler zaten aynıysa işlem yapma
        if list(self.get_hsv) != args[1]:
            self.biswindow.ronk.hsv = args[1]
            self.biswindow.renk_guncelle()

    def on_rgb2(self, *args):
        # Gelen değerler ile varolan değerler zaten aynıysa işlem yapma
        if list(self.get_rgb) != args[1]:
            self.biswindow.ronk.rgb = args[1]
            self.biswindow.renk_guncelle()

    def on_rgba2(self, *args):
        # Gelen değerler ile varolan değerler zaten aynıysa işlem yapma
        if list(self.get_rgba) != args[1]:
            self.biswindow.ronk.rgba = args[1]
            self.biswindow.renk_guncelle()


class BisColorWindow(BisWindow):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    def __init__(self, **kwargs):
        self.ronk = Color(.8, .8, .8, .7)
        super(BisColorWindow, self).__init__(**kwargs)

    def renk_guncelle(self, *args):
        self.r = round(self.ronk.r, 6)
        self.g = round(self.ronk.g, 6)
        self.b = round(self.ronk.b, 6)

        self.a = round(self.ronk.a, 6)

        self.h = round(self.ronk.h, 6)
        self.s = round(self.ronk.s, 6)
        self.v = round(self.ronk.v, 6)
        self.hex = get_hex_from_color(self.ronk.rgba).upper()

        # Widget değerleri güncellenir
        if self.r != self.ids.renk_r.prop_value: self.ids.renk_r.prop_value = self.r
        if self.g != self.ids.renk_g.prop_value: self.ids.renk_g.prop_value = self.g
        if self.b != self.ids.renk_b.prop_value: self.ids.renk_b.prop_value = self.b

        if self.a != self.ids.renk_a.prop_value: self.ids.renk_a.prop_value = self.a

        if self.h != self.ids.renk_h.prop_value: self.ids.renk_h.prop_value = self.h
        if self.s != self.ids.renk_s.prop_value: self.ids.renk_s.prop_value = self.s
        if self.v != self.ids.renk_v.prop_value: self.ids.renk_v.prop_value = self.v
        if self.v != self.ids.renk_v_slid.value: self.ids.renk_v_slid.value = self.v
        if self.hex != self.ids.renk_hex.prop_text: self.ids.renk_hex.prop_text = self.hex

        # Skalada, RGB konumunu hesapla
        # h -> Hue          -> Açı
        # s -> Saturation   -> Merkeze Uzaklık
        # v -> Value        -> Koyuluk

        aci = self.ronk.h * 2 * math.pi
        x = math.sin(aci) * self.ronk.s
        y = math.cos(aci) * self.ronk.s
        self.nokta = [x, y]

    def renk_skala(self, event, center, width):
        """Çember Skaladan seçim yapılırken işletilir"""
        gen = center[0] - event.x
        yuk = center[1] - event.y
        hip = math.sqrt(gen * gen + yuk * yuk) / (width / 2)

        if hip > 1: hip = 1
        if hip < 0: hip = 0

        rad = (math.atan2(gen, yuk) / math.pi) / 2

        if rad < 0: rad = 1 - abs(rad)

        self.ronk.h = rad
        self.ronk.s = hip
        self.renk_guncelle()

    def renk_sb(self, event, pos, size):
        """Siyah Beyaz Dik Skaladan seçim yapılırken işletilir"""
        v = (event.y - pos[1]) / size[1]

        if v > 1 or v < 0: return
        self.ronk.v = v
        self.renk_guncelle()

    def renk_hex(self, renk_hex):
        try:
            for j, i in enumerate(get_color_from_hex(renk_hex)):
                if j == 0: self.ronk.r = i
                if j == 1: self.ronk.g = i
                if j == 2: self.ronk.b = i
                if j == 3: self.ronk.a = i
        except:
            pass
        self.renk_guncelle()

    def renk_random(self):
        self.ronk.rgb = get_random_color()
        self.renk_guncelle()


class BisColorPicker(ModalView):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    def on_open(self):
        Window.set_system_cursor("hand")
        self.ata.renk_guncelle()

    def on_touch_down(self, touch):
        if touch.button != "right":
            return
            Window.set_system_cursor("wait")
            o = int(Window.left + touch.x), int(Window.top + Window.height - touch.y)
            #_p = ImageGrab.grab((o[0], o[1], o[0] + 1, o[1] + 1)).getpixel((0, 0))

            #self.ata.ronk.r = _p[0] / 255
            #self.ata.ronk.g = _p[1] / 255
            #self.ata.ronk.b = _p[2] / 255
            #self.ata.renk_guncelle()

        Window.set_system_cursor("arrow")
        super(BisColorPicker, self).on_touch_down(touch)
        return True
