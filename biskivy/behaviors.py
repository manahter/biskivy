"""
.. versionchanged:: 18.05.2020
    Verisyon takip tarihi eklendi
"""

from kivy.properties import BooleanProperty, ObjectProperty
from kivy.core.window import Window


class HoverBehaviorS1(object):
    """
    on_enter        -> Fare, ata'ın üstüne geldiğinde 1 kere..
    on_leave        -> Fare, ata'ın üstünden ayrıldığında 1 kere ... çalışır

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """

    disabled = BooleanProperty(False)
    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(HoverBehaviorS1, self).__init__(**kwargs)
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        self.on_disabled()

    def on_disabled(self, *args):
        """Eğer pasifse, boşuna çalışıpta kaynak tüketmesin"""
        if not self.disabled:
            Window.bind(mouse_pos=self.on_mouse_pos)
        else:
            Window.unbind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


class HoverBehaviorS2(object):
    """
    on_enter        -> Fare, ata'ın üstüne geldiğinde 1 kere..
    on_leave        -> Fare, ata'ın üstünden ayrıldığında 1 kere ... çalışır

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi
    """

    # disabled = BooleanProperty(False)
    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    hover_mesafe_x = 0
    hover_mesafe_y = 0

    def __init__(self, **kwargs):
        super(HoverBehaviorS2, self).__init__(**kwargs)
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        self.on_disabled()

    def collide_point_yeni(self, x, y):
        return self.x - self.hover_mesafe_x <= x <= self.right + self.hover_mesafe_x and \
               self.y - self.hover_mesafe_y <= y <= self.top + self.hover_mesafe_y

    def on_disabled(self, *args):
        """Eğer pasifse, boşuna çalışıpta kaynak tüketmesin"""
        if not self.disabled:
            Window.bind(mouse_pos=self.on_mouse_pos)
        else:
            Window.unbind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent

        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point_yeni(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

from kivy.graphics import Color, Line


from kivy.factory import Factory

Factory.register('HoverBehaviorS1', HoverBehaviorS1)
Factory.register('HoverBehaviorS2', HoverBehaviorS2)
