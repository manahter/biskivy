# __all__ = 'BisWindow'

from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.lang import Builder

from biskivy.uix.ortak.wiarc import WiARC

"""
BisWindow:
    BisWinBar
    BisWinKasa
        Widget1
        Widget2
        Widget3
"""

Builder.load_string("""
<BisWinBar>:
<BisWinKasa>:
<BisWinSizer>:

<BisWindow>:
    orientation: "vertical"
    size_hint: None, None
    
    prop_title: ""
    prop_padding: 10, 0, 10, 10
    prop_spacing: 10
    prop_width: 260
    prop_height: None
    prop_height_kasa: self.prop_height - bar.height - self.spacing - 1 if self.prop_height else 0
    
    prop_bgcolor_title: .122, .122, .122, .937
    prop_bgcolor_kasa: .122, .122, .122, .937
    
    width: self.prop_width
    # Pencere içeriğinin yüksekliği, Yükseklik Sınırı'ndan
    #   - büyükse -> Yükseklik Sınırını esas al
    #   - küçükse -> İçerik Yüksekliğini esas al
    ic_height: arcwkasa.height + bar.height + self.spacing + 1
    height: min(self.limit_height, self.prop_height) if self.prop_height else min(self.limit_height, self.ic_height)
    #height: min(self.limit_height, self.ic_height)
    
    ################################ Dragging
    drag_rectangle: [winlabel.x, winlabel.y, winlabel.width, winlabel.height]
    drag_timeout: 1000
    drag_distance: 5
    ##########################################
        
    spacing: 1
    BisWinBar:
        id: bar
        size_hint: 1, None
        height: winlabel.height
        width: self.minimum_width
        padding: 3, 0
        spacing: 3
        
        canvas.before:
            Color:
                rgba: self.parent.prop_bgcolor_title
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [5, 5, 5, 5]
            
        BisIcon:
            id: wiminmax
            prop_icon: bkv.paths.icons.wi_min if self.state == "down" else bkv.paths.icons.wi_max
            color: bkv.prefs.panel.renk_t_item
            on_state:
                self.parent.parent.collapsed = self.state == "down"
        
        BisLabelAligned:
            id: winlabel
            halign: "left"
            prop_text: self.parent.parent.prop_title
            
            # Double touch -> Collapse
            on_touch_down:
                if  self.collide_point(*args[1].pos) and args[1].is_double_tap: \
                    wiminmax.state = ("normal" if wiminmax.state == "down" else "down")
                
        BisIcon:
            id: pinned
            prop_icon: bkv.paths.icons.pinned if self.state == "down" else bkv.paths.icons.unpinned
            color: bkv.prefs.panel.renk_t_item
            on_state:
                self.parent.parent.pinned = self.state == "down"
                        
    # Pencere küçük gelirse, farenin orta tuşu ile kaydırma kullanılabilir
    BisWinKasa:
        do_scroll_x: False
        do_scroll_y: True 
        scroll_type: ['bars']
        
        #bar_pos_y: "left"
        #bar_width: 4
        #effect_cls: "ScrollEffect"
        
        canvas.before:
            Color:
                rgba: self.parent.prop_bgcolor_kasa
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [5, 5, 5, 5]
        
        BoxLayout:
            id: arcwkasa
            
            renk_inner: (.122, .122, .122, .937)
            
            orientation: self.parent.parent.prop_orientation
            padding: self.parent.parent.prop_padding
            spacing: self.parent.parent.prop_spacing
            size_hint: 1, None
            height: self.parent.parent.prop_height_kasa if self.parent.parent.prop_height else self.minimum_height
    
    BisWinSizer:
        size_hint: None, None
        size: 0, 0
        WiDrag:
            id: genles
            size_hint: None, None
            opacity: .5
            pos: self.parent.parent.right - self.width, self.parent.y
            source: bkv.paths.icons.sizer
            size: bar.height/2, bar.height/2
            dragging_func_start: self.parent.parent.on_genles_start
            dragging_func: self.parent.parent.on_genles
            
            color: bkv.prefs.panel.renk_t_item
""")


class _BisWinParent(FloatLayout):
    """Ara değer"""


class BisWindow(WiARC, DragBehavior, BoxLayout):
    """Birazcık açıklama
        :Parameters:
            `ata`: parent widget
                Genelde buton vs olabilir. Bu widget konum oluşturulurken kullanılıyor.
                Mesela BisWindow, ataButon'un altında mı, sağında mı neresinde olacak
                hesaplanır.

            'prop_spacing': 10
                Kasa içine eklenen nesneler arasındaki boşluk.

            'prop_padding': 10, 0, 10, 10
                Kasanın içten kenar boşlukları

            'prop_width': 260
                BisWindow'un genişliği

            'prop_align': "auto"
                BisWindow, parent'ın ne tarafında açılsın
                Seç; auto, left, right, top, bottom

            'pinned': False
                BisWindow'i iğnele/uzaklaşınca kaybet
                Read Only

            'collapsed': False
                BisWindow boyutunu Minimize/Normalize et


        :Usage:
            btn = Button(text="Open Window")

            win = BisWindow()
            win.prop_spacing = 0
            win.prop_padding = 0, 0, 0, 0
            win.prop_width = 400
            win.ata = btn


        .. versionchanged:: 18.05.2020
            Versiyon takip tarihi eklendi

        .. versionchanged:: 24.05.2020
            BisWindow, Pencerenin alt ve üstünden taşmaz. Kaybolmaz. Scroll'lanır.

        .. versionchanged:: 30.05.2020
            BisWindow'da Bar ile Kasa bölündü. Araya spacing koyuldu. Kenarlar yuvarlatıldı
    """

    kasa = None
    """BisWindow'e eklenen öğeler bunun içine aktarılır.
    iptal / Şuan kullanım dışı
    """

    ata = ObjectProperty(None, allownone=True, rebind=True)
    """Parent widget ( sahte parent )
    Genelde buton vs olabilir. 
    * Konum oluşturulurken kullanılıyor. Mesela BisWindow, 
        ataButon'un altında mı, sağında mı neresinde olacak hesaplanır.
    * Bu widget ile eylemsel iletişim kurulur"""

    opened = BooleanProperty(False)
    """BisWindow'i Aç/Kapat"""

    pinned = BooleanProperty(False)
    """BisWindow'i iğnele/uzaklaşınca kaybet"""

    collapsed = BooleanProperty(False)
    """BisWindow boyutunu Minimize/Normalize et"""

    __collapsed_data = {}
    """BisWindow boyutunu Minimize/Normalize ederken, bazı verileri tutar"""

    hovered = BooleanProperty(False)
    """BisWindow'in üstüne gelindi mi? Yanlızca oku"""

    limit_height = NumericProperty(1000)
    """Window, pencerenin kenarlarından çıkıpta kaybolmasın diye ayarlandı.
    Otomatik hesaplanır.
    Pencerenin yukarıdan ve aşağıdan çıkması engellendi.
    Henüz Pencerenin sağ ve solunda çıkmalar engellenmedi. İleride onlar da
    ayarlanacak."""

    prop_align = StringProperty("auto")
    """BisWindow, parent'ın ne tarafında açılsın
        auto -> default
        left, right, top, bottom"""

    prop_orientation = StringProperty("vertical")
    """BisWindow'un (Kasasının) içindekiler hangi yönde dizilsin?
    """

    # İptal
    yakinlik = 20
    """Window kenarlarına en fazla kaç piksel yakın olabilir.
    bu kadar pikselden sonra, BisWindow küçülmeye başlar.."""

    __events__ = ('on_pre_open', 'on_open', 'on_pre_close', 'on_close', 'on_enter', 'on_leave')

    def __init__(self, ata=None, **kwargs):
        # WiARC -> Add, Remove, Clear Widget işlemleri için kolaylaştırıcı
        # Sadece BisWinBar, BisWinKasa tiplerini selfe ekle. Diğerlerini kasaya ekle
        self.wiarc_accepted_widgets = (BisWinBar, BisWinKasa, BisWinSizer)

        # Boyut değiştikçe, yüksekliği hesapla
        Window.bind(on_resize=self.on_y)

        super(BisWindow, self).__init__(**kwargs)
        self.ata = ata
        self._float_parent = _BisWinParent()
        self.parent = None
        self.opacity = 0

    def __konum_hesapla(self):
        if not self.ata:
            Logger.warning('BisWindow: cannot open view, no ata found. Please enter -> self.ata = your_widget')
            self.pos = (Window.width - self.width) / 2, (Window.height - self.height) / 2
            self.on_y()
            return
        ata = self.ata

        # Ata'nın Global pozisyonu bulunur. Ata genelde bir butondur veya ColorButon tarzıdır.
        ata_x, ata_y = ata.to_window(*ata.pos)
        farkx, farky = self._float_parent.to_window(*self._float_parent.pos)

        ata_x = int(ata_x - farkx)
        ata_y = int(ata_y - farky)

        # Menü, butonun ne tarafında açılacak
        _align = ata.prop_align if hasattr(ata, "prop_align") else self.prop_align

        if _align in ["auto", "top", "bottom"]:
            # Butonun üst tarafındaki boşluk bulunur
            ust_bosluk = Window.height - ata_y - ata.height

            # Butonun alt tarafındaki boşluk bulunur
            alt_bosluk = ata_y

            yan_bosluk = int(ata_x if Window.width - ata_x > ata_x else ata_x + ata.width - self.width)

            # Auto -> Alt/Üst boşluktan büyük olan tarafı seç
            if _align == "auto":
                _align = "top" if ust_bosluk > alt_bosluk else "bottom"

            # Window üst boşlukta
            if _align == "top":
                self._taban = int(ata_y + ata.height)
                self.pos = yan_bosluk, int(ata_y + ata.height)
                self.on_y()
            else:
                self.pos = yan_bosluk, int(alt_bosluk - self.height)

        else:
            # Butonun üst tarafındaki boşluk bulunur
            ust_bosluk = Window.height - ata_y

            # Butonun alt tarafındaki boşluk bulunur
            alt_bosluk = ata_y

            # Window Sağ boşlukta
            if _align == "right":
                self_x = int(ata_x + ata.width)
            # Window Sol boşlukta
            else:
                self_x = int(ata_x - self.width)

            if alt_bosluk > ust_bosluk:
                self.pos = self_x, int(ata_y + ata.height)
            else:
                self._taban = ata_y
                self.pos = self_x, ata_y
                self.on_y()

    def open(self):
        self.opened = True

    def close(self):
        self.opened = False

    def toggle(self, force=True):
        """
        open ise close yap
        close ise open yap
        :param force: True -> Pinned olsa bile değiştir.
        :return:
        """
        if force:
            self.ids.pinned.state = "normal"
        self.opened = not self.opened

    def on_opened(self, *args):
        # "Ata yoksa Bitir" iptal edildi
        #if self.ata is None:
        #    Logger.warning('BisWindow: cannot open view, no ata found. Please enter -> self.ata = your_widget')
        #    return

        if self.pinned:
            if not self.opened:
                self.opened = True
            return

        self.ids.wiminmax.state = "normal"

        if self.opened:
            Logger.info(f"{self.__class__.__name__}: Opened")

            # Parent'ı kontrol et
            self.on_parent()

            # Open öncesi fonksiyon varsa işlet
            self.dispatch('on_pre_open')

            # Open
            Window.add_widget(self._float_parent)
            Window.bind(on_pos=self.__konum_hesapla, on_keyboard=self._handle_keyboard)

            # Konum Hesapla
            self.__konum_hesapla()

            # Görünür kıl
            self.opacity = 1

            # Mouse Position takipi etkinleştir
            Window.bind(mouse_pos=self.on_mouse_pos)

            # Open sonrası fonksiyon varsa işlet
            self.dispatch('on_open')

        else:
            Logger.info("BisWindow Closed")

            # Görünmez kıl
            self.opacity = 0

            # Mouse Position takip iptal
            Window.unbind(mouse_pos=self.on_mouse_pos)

            # Close öncesi fonksiyon varsa işlet
            self.dispatch('on_pre_close')

            # Close
            Window.remove_widget(self._float_parent)
            Window.unbind(on_pos=self.__konum_hesapla, on_keyboard=self._handle_keyboard)

            # Close sonrası fonksiyon varsa işlet
            self.dispatch('on_close')

            # Limit_height'i temizle
            self.height = self.limit_height = self.ic_height

    _last_height = None
    """Son kullanılan self.height değerini tutar"""
    def on_height(self, *args):
        """Yükseklik değiştiğinde,
        BisWindow'i üst tarafından hizalı olacak şekilde küçült/büyüt"""

        # Yükselik Bar'dan küçük olamaz
        if self.height < self.ids.bar.height + self.spacing:
            self.height = self.ids.bar.height + self.spacing + 1
            return

        # Yükseklik değiştiğinde, üst taraftan hizalı şekilde büyüklüğü ayarlar.
        if self._last_height:
            self.y += self._last_height - self.height
        self._last_height = self.height

    _taban = 0
    """self için kullanılan taban değeri. 
    Yani, self, bu hizadan aşağıya geçemez ve küçülür"""
    def on_y(self, *args):
        if not self.parent:
            return

        if self.collapsed:
            if self.y < self._taban:
                self.y = self._taban
            return

        if self.top > Window.height:
            self.top = Window.height

        if self.y < self._taban:
            self.limit_height = self.height + self.y - self._taban
        else:
            self.limit_height = self.top - self._taban

        if self.limit_height < self.ids.bar.height:
            self.limit_height = self.ids.bar.height
            self.y = self._taban

    def on_collapsed(self, *args):
        # BisWindow pinlenmemişse pinle
        if not self.pinned:
            self.ids.pinned.state = "down"

        # Üst taraftan sabit şekilde büyülüp küçülsün
        top = self.top

        # Kasa kısa erişim için
        kasa = self.ids.arcwkasa

        # Küçült
        if self.collapsed:
            self.__collapsed_data = {"opacity": kasa.opacity, "height": kasa.height}
            kasa.disabled = True
            kasa.opacity = 0
            kasa.height = 0
            if self.prop_height:
                self.height = 0
        # Büyült
        else:
            kasa.disabled = False
            kasa.height = self.__collapsed_data.pop("height", kasa.minimum_height)
            kasa.opacity = self.__collapsed_data.pop("opacity", 1)

        # Üst taraftan sabit şekilde büyülüp küçülsün
        self.top = top

    def on_genles_start(self, touch):
        # Genleşme başlamadan önce, mevcut size değerleri kaydedilir
        touch.width = self.width
        touch.height = self.height

    def on_genles(self, touch):
        # Minimize edilmişse genleşme iptal
        if self.collapsed:
            return

        # Pinlenmemişse pinle
        if not self.pinned:
            self.ids.pinned.state = "down"

        # Kaydırılan genişliği hesapla
        width = touch.width + touch.x - touch.down_x

        # Genişlik, bar'ın minimum genişliğinden küçük olamaz
        self.width = max(width, self.ids.bar.minimum_width)

        if self.prop_height:
            height = touch.height - touch.y + touch.down_y
            self.prop_height = max(height, self.ids.bar.minimum_height + self.spacing + 1)


    def on_parent(self, *args):
        """Parent değiştiğinde, parent'ı kontrol eder.
        Parent'ın -> '_BisWinParent' olması beklenir.
        Parent -> '_BisWinParent' değilse, başka bir Widget ise,
        o Widget tetikleyici widget olarak kabul edilir.
        Bundan dolayı;
            self.ata -> Widget  olarak ayarlanır.

        """
        # Parent yoksa, _BisWinParent'ımıza ekleyelim
        if not self.parent:
            self._float_parent.add_widget(self)

        # Parent _BisWinParent değilse, onu atamız yapalım.
        if not isinstance(self.parent, _BisWinParent):
            if not self.ata:
                self.ata = self.parent
            self.parent = None

    def on_ata(self, *args):
        if not self.ata:
            return
        self.ata.bind(on_press=self.toggle)

    def on_prop_align(self, *args):
        self.__konum_hesapla()

    def on_mouse_pos(self, *args):
        # posizyon okunur
        pos = args[1]

        # içerde mi dışarda mı kontrol edilir
        inside = self.collide_point(*self.to_widget(*pos))

        if self.hovered == inside:
            # Zaten önceki seferkiyle aynıysa işlem yapma
            return
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_touch_down(self, touch):
        if not self.opened:
            super().on_touch_down(touch)
            return False

        if self.hovered:
            # Self'i ön plana getiriyoruz..
            Window.remove_widget(self._float_parent)
            Window.add_widget(self._float_parent)
            super().on_touch_down(touch)
            return True

        elif not self.pinned:
            self.close()
            super().on_touch_down(touch)
            return False

        super(BisWindow, self).on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        if not self.opened:
            super().on_touch_move(touch)
            return False

        if self._drag_touch:
            self.ids.pinned.state = "down"
            if self._taban:
                self._taban = 0

        super(BisWindow, self).on_touch_move(touch)
        return False

    def on_touch_up(self, touch):
        if not self.opened:
            super().on_touch_up(touch)
            return False
        super(BisWindow, self).on_touch_up(touch)
        return False

    def on_pre_open(self):
        pass

    def on_open(self):
        pass

    def on_pre_close(self):
        pass

    def on_close(self):
        pass

    def on_enter(self):
        pass

    def on_leave(self):
        self.close()

    def _handle_keyboard(self, window, key, *largs):
        if key == 27:
            self.close()
            return True


class BisWinBar(BoxLayout):
    pass


class BisWinKasa(ScrollView):
    pass


class BisWinSizer(FloatLayout):
    pass