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
        BisButton:
            prop_text: "Text BisButton"
            on_press: 
                print(bkv.prefs.button.renk_selected)
                #app.prefs.button.aha["a"]["b"] = 5
                #app.prefs.button.renk_selected = [0.7, 0.503, 0.561, 0.902]
        BisButton:
            prop_text: "Text + Icon BisButton"
            prop_icon: bkv.paths.icons.menu
                                
        BisCombinLayout:
            BisButton:
                prop_icon: bkv.paths.icons.azalt
            BisButton:
                prop_icon: bkv.paths.icons.arti
            BisButton:
                prop_icon: bkv.paths.icons.carpi
            BisButton:
                prop_icon: bkv.paths.icons.eksi
            BisButton:
                prop_icon: bkv.paths.icons.artir
                
        BisCombinLayout:
            BisButton:
                prop_text: "Horizontal"
            BisButton:
                prop_text: "Combine"
            BisButton:
                prop_text: "BisButton"
                
        BisCombinLayout:
            orientation: "vertical"
            BisButton:
                prop_text: "Vertical"
            BisButton:
                prop_text: "Combine"
            BisButton:
                prop_text: "BisButton"
        
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
