from kivy.core.window import Window
from kivy.lang import Builder

from biskivy.behaviors import HoverBehaviorS1

Builder.load_string("""
<BisDivider>:
    prop_minimum_size: 30
    yatay: self.parent.orientation == "vertical"
    size_hint: [1, None] if self.yatay else [None, 1]
    size: 5, 5
    #canvas:
    #    Color:
    #        rgb: 1,1,1
    #    Rectangle:
    #        pos: self.pos
    #        size: self.size
""")


class _Empty:
    pass

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class BisDivider(HoverBehaviorS1, FloatLayout):
    """
    * Standart Label sayılır
    """
    # Kaydırma esnasında, önceki ve sonraki widget'ların dataları tutulur
    touch_data = None

    def on_enter(self):
        Window.set_system_cursor("size_we" if self.size_hint[1] else "size_ns")

    def on_leave(self):
        # Burayı düzelt!!! ColorPicker'ın cursor şekli bozuluyor..
        if not self.touch_data:
            Window.set_system_cursor("arrow")

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # Kendi indeximizi bulalım
            ind = self.parent.children.index(self)

            # Öncemizdeki widget'ı bulalım
            onceki_widget = self.parent.children[ind+1] if ind < len(self.parent.children) else None

            # Sonramızdaki widget'ı bulalım
            sonraki_widget = self.parent.children[ind-1] if 0 < ind else None

            # Eğer öncemizde veya sonramızda widget yoksa, işlem iptal
            if not (onceki_widget and sonraki_widget):
                super().on_touch_down(touch)
                return False

            # Bu widget'ı tut
            touch.grab(self)

            self.touch_data = _Empty()
            self.touch_data.x = touch.x
            self.touch_data.y = touch.y

            self.touch_data.onceki = onceki_widget
            self.touch_data.onceki_size = onceki_widget.size.copy()
            self.touch_data.onceki_hint = onceki_widget.size_hint.copy()
            self.touch_data.sonraki = sonraki_widget
            self.touch_data.sonraki_size = sonraki_widget.size.copy()
            self.touch_data.sonraki_hint = sonraki_widget.size_hint.copy()

            # Hint olup olmadığı kontrol edilecek
            hint = None

            # Widget'ların hint'i olup olmadığına bakıyoruz
            if self.yatay:
                if onceki_widget.size_hint[1] is not None and sonraki_widget.size_hint[1] is not None:
                    hint = onceki_widget.size_hint[1] + sonraki_widget.size_hint[1]
                    onceki_widget.size_hint_y = None
                    sonraki_widget.size_hint_y = None

            else:
                if onceki_widget.size_hint[0] is not None and sonraki_widget.size_hint[0] is not None:
                    hint = onceki_widget.size_hint[0] + sonraki_widget.size_hint[0]
                    onceki_widget.size_hint_x = None
                    sonraki_widget.size_hint_x = None

            self.touch_data.hint = hint

            super().on_touch_down(touch)
            return True

        super().on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            fark_x = self.touch_data.x - touch.x
            fark_y = self.touch_data.y - touch.y

            if self.yatay:
                onceki_x = self.touch_data.onceki_size[1] + fark_y
                sonraki_x = self.touch_data.sonraki_size[1] - fark_y

                if onceki_x <= self.prop_minimum_size:
                    onceki_x = 0
                    sonraki_x = self.touch_data.onceki_size[1] + self.touch_data.sonraki_size[1]
                elif sonraki_x <= self.prop_minimum_size:
                    sonraki_x = 0
                    onceki_x = self.touch_data.onceki_size[1] + self.touch_data.sonraki_size[1]

                self.touch_data.onceki.height = onceki_x
                self.touch_data.sonraki.height = sonraki_x
            else:
                onceki_x = self.touch_data.onceki_size[0] - fark_x
                sonraki_x = self.touch_data.sonraki_size[0] + fark_x

                if onceki_x <= self.prop_minimum_size:
                    onceki_x = 0
                    sonraki_x = self.touch_data.onceki_size[0] + self.touch_data.sonraki_size[0]
                elif sonraki_x <= self.prop_minimum_size:
                    sonraki_x = 0
                    onceki_x = self.touch_data.onceki_size[0] + self.touch_data.sonraki_size[0]

                self.touch_data.onceki.width = onceki_x
                self.touch_data.sonraki.width = sonraki_x

            super().on_touch_down(touch)
            return True
        super().on_touch_down(touch)
        return False

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            #Window.set_system_cursor("arrow")

            if self.touch_data.hint:
                if self.yatay:
                    toplam_height = (self.touch_data.onceki.height + self.touch_data.sonraki.height)
                    self.touch_data.onceki.size_hint_y = (self.touch_data.onceki.height / toplam_height) * self.touch_data.hint
                    self.touch_data.sonraki.size_hint_y = (self.touch_data.sonraki.height / toplam_height) * self.touch_data.hint
                else:
                    toplam_width = self.touch_data.onceki.width + self.touch_data.sonraki.width
                    self.touch_data.onceki.size_hint_x = (self.touch_data.onceki.width / toplam_width) * self.touch_data.hint
                    self.touch_data.sonraki.size_hint_x = (self.touch_data.sonraki.width / toplam_width) * self.touch_data.hint

            self.touch_data = None

            super().on_touch_down(touch)
            return True

        super().on_touch_down(touch)
        return False

    #def on_mouse_pos(self, *args):
    #    if self.touch_data:
    #        super().on_mouse_pos(*args)
    #        return True

    #    super().on_mouse_pos(*args)
    #    return False