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
        BisToggleButton:
            group: "tercih0"
            prop_text: "Text BisToggleButton"
            state: 'down'
            
        BisToggleButton:
            group: "tercih0"
            prop_text: "Text + Icon BisToggleButton"
            prop_icon: bkv.paths.icons.menu
                
        BisCombinLayout:
            BisToggleButton:
                group: "tercih1"
                prop_icon: bkv.paths.icons.azalt
            BisToggleButton:
                group: "tercih1"
                prop_icon: bkv.paths.icons.arti
            BisToggleButton:
                group: "tercih1"
                prop_icon: bkv.paths.icons.carpi
                state: 'down'
            BisToggleButton:
                group: "tercih1"
                prop_icon: bkv.paths.icons.eksi
            BisToggleButton:
                group: "tercih1"
                prop_icon: bkv.paths.icons.artir
                
        BisCombinLayout:
            BisToggleButton:
                group: "tercih2"
                prop_text: "Horizontal"
            BisToggleButton:
                group: "tercih2"
                prop_text: "Combine"
            BisToggleButton:
                group: "tercih2"
                prop_text: "BisToggleButton"
                state: 'down'
                
        BisCombinLayout:
            orientation: "vertical"
            BisToggleButton:
                group: "tercih3"
                prop_text: "Vertical"
            BisToggleButton:
                group: "tercih3"
                prop_text: "Combine"
            BisToggleButton:
                group: "tercih3"
                prop_text: "BisToggleButton"
                state: 'down'
        
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
