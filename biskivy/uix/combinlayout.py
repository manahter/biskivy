from kivy.lang import Builder

from biskivy.uix.boxlayout import BisBoxLayout


Builder.load_string("""
<BisCombinLayout>:
    spacing: 1
    size_hint: 1, None
    height: self.minimum_height
    
    prop_orientation: "horizontal"
    orientation: self.prop_orientation
""")


class BisCombinLayout(BisBoxLayout):
    """
    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi

    .. versionchanged:: 23.05.2020
        Class ismi değiştirildi.
        Konum değiştirildi
    """
    def on_size(self, *args):
        if len(self.children) > 1:
            for i in self.children:
                i.tek = False
                i.yat = self.orientation == "horizontal"
                i.dik = self.orientation == "vertical"

            self.children[0].son = True
            self.children[-1].bas = True
