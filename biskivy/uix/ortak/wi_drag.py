from kivy.properties import DictProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
Builder.load_string("""
<WiDrag>:
    # Alttaki çalışıyor. Eğer resim yoksa, bu widget görünmez olur
    #opacity: 0 if not self.source else 1
""")


class WiDrag(Image):
    dragging_data = DictProperty()

    dragging_func_start = None
    dragging_func = None
    dragging_func_stop = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # self'i tuttuk.
            touch.grab(self)
            self.dragging_data["down_x"] = int(touch.x)
            self.dragging_data["down_y"] = int(touch.y)
            self.draggin_event(self.dragging_func_start)
            super().on_touch_down(touch)
            return True
        super().on_touch_down(touch)
        return False

    def on_touch_move(self, touch):
        # Eğer self tutulduysa
        if touch.grab_current is self:
            # Calling func
            self.dragging_data["x"] = touch.x
            self.dragging_data["y"] = touch.y
            self.draggin_event(self.dragging_func)
            super().on_touch_move(touch)
            return False
        super().on_touch_move(touch)
        return False

    def on_touch_up(self, touch):
        # Eğer self tutulduysa
        if touch.grab_current is self:
            # self'i bırak
            touch.ungrab(self)
            # Last call func
            self.dragging_data["x"] = touch.x
            self.dragging_data["y"] = touch.y
            self.dragging_data["up_x"] = touch.x
            self.dragging_data["up_y"] = touch.y
            self.draggin_event(self.dragging_func_stop)
            self.dragging_data.clear()
            super().on_touch_up(touch)
            return True

        super().on_touch_up(touch)
        return False

    def draggin_event(self, func):
        if not func:
            return
        if type(func) in (list, tuple):
            func[0](self.dragging_data, *func[1:])
        else:
            func(self.dragging_data)
