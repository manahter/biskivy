from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from biskivy.uix.ortak.wiarc import WiARC
from biskivy.uix.boxlayout import BisBoxLayout

Builder.load_string("""
<BisScrollBoxLayoutBack>:

<BisScrolledBoxLayout>:
    prop_orientation: "vertical"
    size_hint_y: 1
    x: int(self.x)
    y: int(self.y)
    BisScrollBoxLayoutBack:
        orientation: self.parent.prop_orientation
        id: arcwkasa
        padding: 10,
        spacing: 10
""")


class BisScrollBoxLayoutBack(BisBoxLayout):
    pass


class BisScrolledBoxLayout(WiARC, ScrollView):

    def __init__(self, **kwargs):
        self.wiarc_accepted_widgets = (BisScrollBoxLayoutBack, )
        #self.wiarc_accepted_to_kasa = True
        super(BisScrolledBoxLayout, self).__init__(**kwargs)
