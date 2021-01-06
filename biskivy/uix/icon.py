from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_string("""
<BisIcon>:
    prop_icon: ""
    
    source: self.prop_icon
    size_hint: None, None
    size: self.parent.height,self.parent.height
    #size: int(self.parent.height), int(self.parent.height)
""")


class BisIcon(ToggleButtonBehavior, Image):
    pass
