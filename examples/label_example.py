from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

import biskivy

Window.size = (500, 500)
Window.clearcolor = (.22, .22, .22, 1)

root = Builder.load_string("""
FloatLayout:
    BoxLayout:
        orientation: "vertical"
        spacing: 5
        size_hint: .5, None
        height: self.minimum_height
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        #######################################################
        #################################### These are examples
        BisLabel:
            prop_text: "BisLabel -> Standart"
            
        BisLabelAligned:
            prop_text: "BisLabelAligned -> Left"
            halign: "left"
            
        BisLabelAligned:
            prop_text: "BisLabelAligned -> Center"
            halign: "center"
            
        BisLabelAligned:
            prop_text: "BisLabelAligned -> Right"
            halign: "right"
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
