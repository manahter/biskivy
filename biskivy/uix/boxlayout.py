from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
Builder.load_string("""
<BisBoxLayout>:
    size_hint_y: None
    height: self.minimum_height
    
    prop_orientation: "horizontal"
    orientation: self.prop_orientation
""")


class BisBoxLayout(BoxLayout):
    pass
