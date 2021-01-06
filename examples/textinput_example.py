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
        BisTextInput:
            prop_text: "Bildiğin Metin girişi"
            
        BisTextInput:
            prop_text: "Ortalı Metin İptal"
            
        BisCombinLayout:
            BisTextInput:
                prop_text: "BisButton(Button) ile birleştiririlebilir"
            BisButton:
                prop_icon: bkv.paths.icons.menu
                prop_only_icon: True
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
