from kivy.lang import Builder

from biskivy.uix.panel import BisPanel

Builder.load_string("""
<BisWinPrefInterfaces>:
    orientation: "vertical"
    BisPanelItem:
        prop_title: "Display"
        BisBoxLayout:
            spacing: 5
            BisLabelAligned:
                prop_text: "Resolution Scale"
            BisNumberInput:
                prop_min: 1
                prop_max: 10
                prop_step: .1
                prop_value: bkv.prefs.scale.size
                prop_default: 1
                on_prop_value: bkv.prefs.scale.size = round(self.prop_value, 3)
        BisBoxLayout:
            spacing: 5
            BisLabelAligned:
                prop_text: "Text Resolution"
            BisNumberInput:
                prop_type: int
                prop_min: 6
                prop_max: 64
                prop_step: 1
                prop_value: bkv.prefs.scale.font
                prop_default: 13
                on_prop_value: bkv.prefs.scale.font = round(self.prop_value, 3)
                
    BisPanelItem:
        prop_title: "Animation"
        
""")


class BisWinPrefInterfaces(BisPanel):
    pass