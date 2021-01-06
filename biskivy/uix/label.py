from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string("""
<BisLabel>:
    prop_text: " "
    text: self.prop_text or " "
    size_hint_y: None
    height: int(self.texture_size[1] + 4)
    
    font_size: bkv.prefs.scale.font_size
    color: bkv.prefs.label.renk_text
    
    on_texture:
        if self.texture: self.texture.min_filter='nearest'
        if self.texture: self.texture.mag_filter='nearest'

<BisLabelAligned>:
    halign: "right"  
    valign: "center"  
    shorten: True           # Küçüldükçe, yazıyı "Xx...xx" gibi kısalt
    text_size: ((None if not self.size_hint_x else self.width) , None)      # Bu şekilde daha doğru. Sakın kısaltma bunu
""")


class BisLabel(Label):
    """
    * Standart Label sayılır
    """


class BisLabelAligned(BisLabel):
    """
    * Sağa sola yaslanabilir Label

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi

    .. versionchanged:: 23.05.2020
        Konum değiştirildi
    """


#class BisLabel2(BisLabel):
#    def on_touch_down(self, touch):
#        if self.collide_point(*touch.pos):
#            # if the touch collides with our widget, let's grab it
#            touch.grab(self)
#
#            # and accept the touch.
#            return True
#
#    def on_touch_up(self, touch):
#        # here, you don't check if the touch collides or things like that.
#        # you just need to check if it's a grabbed touch event
#        if touch.grab_current is self:
#            # ok, the current touch is dispatched for us.
#            # do something interesting here
#            print('Hello world!')
#
#            # don't forget to ungrab ourself, or you might have side effects
#            touch.ungrab(self)
#
#            # and accept the last up
#            return True