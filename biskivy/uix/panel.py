from kivy.properties import BooleanProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.lang import Builder

"""
Kod Yapısı;
    BisPanel:
        BisPanelBack:
            BisPanelKapak:
                BPKImage:
                BPKLabel:
                BPKImage:
            BisPanelKasa:
                BisPanelItem:
                BisPanelItem:
                BisPanelItem:
                BisPanelItem:
                BisPanelItem:
                BisPanelItem:

Kullanım:
    BisPanel:
        BisPanelItem:
            prop_title: "Başlık"
            SomeLayout
        BisPanelItem:
            SomeWidget
            SomeWidget
        BisPanelItem:
            ...
        BisPanelItem:
"""


Builder.load_string("""
#################################################### Panel Header Behavior
# Panel açılılır/kapanır. Bu panelin başlığında, ikona veya 
# yazıya tıkladığımızda, panelin açılıp kapanmasını sağlar.
<BPKBehavior@ButtonBehavior>:
    on_press:
        self.parent.parent.collapse = not self.parent.parent.collapse

<BPKLabel@BPKBehavior+BisLabelAligned>:
<BPKImage@BPKBehavior+Image>:
####################################################



<BisPanelKapak>:  
    size_hint_y: None

    canvas.before:
        Color:
            rgba: bkv.prefs.panel.renk_inner
        Rectangle:
            pos: self.pos
            size: self.size
            
    ### Collapse
    BPKImage:    
        size_hint: None, None
        width: self.parent.height
        height: self.parent.height
        pos: self.parent.pos
        
        source: bkv.paths.icons.panel_closed if self.parent.parent.collapse else  bkv.paths.icons.panel_opened
        color: bkv.prefs.panel.renk_t_item
    
    ### LABEL
    BPKLabel:
        text: self.parent.parent.prop_title
        
        # Size
        width: self.texture_size[0] + dp(40)
        
        # Text özellikleri
        halign: "left"          # Yatay Ortala
        
        # Renk
        color: bkv.prefs.panel.renk_text
        
        # Textsize değiştiğinde, Headerin yüksekliğini buna göre günceller
        on_texture_size:
            self.parent.height = self.height

    ### Tutaç
    BisIcon:
        prop_icon: bkv.paths.icons.tutac
        color: bkv.prefs.panel.renk_t_item
        
        on_state:
            self.parent.parent.collapsed = self.state == "down"
    
        on_parent:
            self.parent.parent.tutac = self
        
        

<BisPanelKasa>:
    orientation: self.parent.prop_orientation or 'horizontal'
    spacing: 0 if self.parent.collapse else 5
    padding: [0,0,0,0] if self.parent.collapse else self.parent.prop_padding
    
    # Size
    size_hint_x: None if self.parent.collapse else 1
    size_hint_y: None
    width: 0 if self.parent.collapse else self.minimum_height
    height: 0 if self.parent.collapse else self.minimum_height
    
    # Show/Hide
    disabled: True if self.parent.collapse else False
    on_parent: 
        self.opacity = 0 if self.parent.collapse else 1
        
    canvas.before:
        Color:
            rgba: (.2,.2,.2,.702)
        Rectangle:
            pos: self.pos
            size: self.size
    
    
<BisPanelItem>:
    # Çerçeve Başlık Metni
    prop_title: "Title"                          
    prop_orientation: "vertical"
    prop_padding: [20,10,20,10]
    
    # 0.1'de güzel. Animasyon hızı
    anim_duration: 0    # 0.1 'de fena değil
    ##############################################################
    
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height

    ################################ Dragging
    drag_rectangle: [self.tutac.x, self.tutac.y, self.tutac.width, self.tutac.height]
    drag_timeout: 10000000
    drag_distance: 5
    dragging: False

    canvas.before:
        Color:
            rgba: bkv.prefs.panel.renk_selected if self.dragging else  bkv.prefs.panel.renk_outline
        Line:
            width: 2 if self.dragging else 1
            rectangle: [*self.pos, *self.size]
            
    BisPanelKapak:
    BisPanelKasa:
        

<BisPanelBack>:
    # ScrollView'de kayabilsin diye, zemin olarak oluşturuldu
    # Şuanları içerir;
    #   BisPanel Kapak
    #   BisPanel Kasa

<BisPanel>:
    do_scroll_x: False
    do_scroll_y: True 
    scroll_type: ['bars']
    bar_width: 4
    effect_cls: "ScrollEffect"
    
    # Bu ikisi sayesinde, bulanıklaşma sorunu oluşmuyor
    x: int(self.x)
    y: int(self.y)
    
    BisPanelBack:
    
        size_hint_y: None
        
        height: self.minimum_height
        orientation: "vertical"
        
        canvas.before:
            Color:
                rgba: bkv.prefs.panel.renk_inner
            Rectangle:
                pos: self.pos
                size: self.size
        
""")


class BisPanel(ScrollView):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    .. versionchanged:: 23.05.2020
        İsim değişikliği -> Mucre -> BisPanel
    """
    _mucre = None

    def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, BisPanelBack):
            super(BisPanel, self).add_widget(widget, index)
            self._mucre = widget
            return

        if self._mucre:
            self._mucre.add_widget(widget, index, canvas)

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ListProperty

class BisPanelBack(FloatLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    minimum_height = NumericProperty(100)
    in_pos = BooleanProperty(False)
    childlist = ListProperty()

    def on_children(self, caller, childrens):
        if self.in_pos:
            return
        #self.set_minimum_size()
        childrens[0].bind(size=self.set_minimum_size)
        childrens[0].bind(pos=self.set_child_pos)
        self.childlist = childrens[::-1]

    def set_minimum_size(self, *args):
        h = 0
        for i in self.children:
            h += i.height

        self.minimum_height = h

        # Tüm alt widget'ların pozisyonları tekrar hesaplanır
        oncekiler_h = 0
        for i in self.childlist[::-1]:
            i.y = oncekiler_h
            i.x = 0
            oncekiler_h += i.height

    def set_child_pos(self, caller, pos):
        if not caller.dragging:
            return

        # self'in indexi bulunur
        imy = self.childlist.index(caller)

        ust_bosluk = self.childlist[imy-1].y - caller.top if imy > 0 else self.height - caller.top
        alt_bosluk = caller.y - self.childlist[imy+1].top if imy < len(self.childlist) - 1 else caller.y

        kayan_item = None

        # Yukarı sürüklüyorsak ve en yukarda değilsek
        if alt_bosluk > ust_bosluk and imy > 0:
            ustteki = self.childlist[imy - 1]
            if alt_bosluk >= ustteki.height:
                kayan_item = ustteki

        elif alt_bosluk < ust_bosluk and imy < len(self.childlist) - 1:
            alttaki = self.childlist[imy + 1]
            if ust_bosluk >= alttaki.height:
                kayan_item = alttaki

        if kayan_item:
            self.childlist.remove(kayan_item)
            self.childlist.insert(imy, kayan_item)

            iu = self.childlist.index(kayan_item)
            y_yuksekligi = 0
            for i in self.childlist[iu+1:]:
                y_yuksekligi += i.height
            Animation(y=y_yuksekligi, x=0, duration=.15).start(kayan_item)


class BisPanelItem(DragBehavior, BoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """
    collapse = BooleanProperty(True)
    kasa = None
    kapak = None
    tutac = None

    def add_widget(self, widget, index=0, canvas=None):
        # Eklenen Widget Kasa ise
        if isinstance(widget, BisPanelKasa):
            super(BisPanelItem, self).add_widget(widget, index, canvas)
            self.kasa = widget
            return

        # Eklenen Widget Kapak ise
        if isinstance(widget, BisPanelKapak):
            super(BisPanelItem, self).add_widget(widget, 1, canvas)
            self.kapak = widget
            return

        # Eklenen Widget hiçbiri değilse, Kasaya koy
        self.kasa.add_widget(widget, index, canvas)

    def on_collapse(self, *args):
        """Animasyonlu, açılır/kapanır"""
        if self.collapse:
            self.kasa.opacity = 0
        anim = Animation(height=0 if self.collapse else self.kasa.minimum_height, duration=self.anim_duration)
        anim.start(self.kasa)
        anim.bind(on_complete=self._on_collapse)
        #self.height = 0 if self.collapse else self.kasa.minimum_height
        #self._on_collapse()

    def _on_collapse(self, *args):
        """Animasyon bittiğinde"""
        if not self.collapse:
            self.kasa.height = self.kasa.minimum_height
            self.kasa.opacity = 1

    def on_touch_down(self, touch):
        if self.tutac and self.tutac.collide_point(*touch.pos):
            # Sürükleme değişkenleri aktif ediliyor
            self.dragging = True
            self.parent.in_pos = True

            # En üste gelsin diye, silinip yeniden eklenir
            p = self.parent
            p.remove_widget(self)
            p.add_widget(self)

        super(BisPanelItem, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.dragging:
            # Sürükleme değişkenleri pasif ediliyor
            self.dragging = False
            self.parent.in_pos = False

            # Sürüklenen widget bırakıldığında, bulunduğu indexe
            # göre belirlenen pozisyonuna animasyonlu gönderilir.
            iu = self.parent.childlist.index(self)
            oncekiler_h = 0
            for i in self.parent.childlist[iu + 1:]:
                oncekiler_h += i.height
            Animation(y=oncekiler_h, x=0, duration=.1).start(self)

        super(BisPanelItem, self).on_touch_up(touch)

    def on_touch_move5(self, touch):
        if self.dragging:
            p = self.parent

            # self'in indexi
            imy = p.children.index(self)
            ustten_en_yakin = None
            alttan_en_yakin = None

            for i in p.children:
                ust_fark = i.top - self.top
                alt_fark = self.y - i.y

                if not ustten_en_yakin and ust_fark > 0:
                    ustten_en_yakin = i
                elif ustten_en_yakin and ustten_en_yakin.top - self.top > ust_fark > 0:
                    ustten_en_yakin = i

                if not alttan_en_yakin and alt_fark > 0:
                    alttan_en_yakin = i
                elif alttan_en_yakin and self.y - alttan_en_yakin.y > alt_fark > -5:
                    alttan_en_yakin = i

            alt_bosluk = self.y - alttan_en_yakin.top if alttan_en_yakin else self.y
            ust_bosluk = ustten_en_yakin.y - self.top if ustten_en_yakin else self.parent.height - self.top

            print(alt_bosluk, ust_bosluk, alttan_en_yakin.prop_title, ustten_en_yakin.prop_title)
            # Yukarı sürüklüyorsak ve en yukarda değilsek
            if alt_bosluk > ust_bosluk:
                if alt_bosluk >= ustten_en_yakin.height:
                    Animation(y=ustten_en_yakin.y - self.height, duration=.1).start(ustten_en_yakin)

            elif alt_bosluk < ust_bosluk and imy > 0:
                if ust_bosluk >= alttan_en_yakin.height:
                    Animation(y=alttan_en_yakin.y + self.height, duration=.1).start(alttan_en_yakin)

        super(BisPanelItem, self).on_touch_move(touch)

    def on_touch_up5(self, touch):
        """Kendimizi, silip tekrar aynı indexe ekliyoruz.
        Konumumuz indexteki sıralamaya göre güncellensin diye bunu yapıyoruz."""
        if self.dragging:
            p = self.parent
            ind = p.children.index(self)
            p.remove_widget(self)
            p.add_widget(self, ind)
            # Eğer bu Widget, tutacından bırakılırsa, dragging'i False yap
            self.dragging = False
        super(BisPanelItem, self).on_touch_up(touch)


class BisPanelKapak(BoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """


class BisPanelKasa(BoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """

