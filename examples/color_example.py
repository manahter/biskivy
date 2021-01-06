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
        BisColor:
            prop_title: "Put Hex"
            hex: "#72FFFFCC"
                            
        BisColor:
            prop_title: "Put HSV"
            hsv: (.4, .7, 1)
        
        BisColor:
            prop_title: "Put RGB"
            rgb: (1, .9, .6)
            
        BisColor:
            prop_title: "Put RGBA"
            rgba: (1, .2, .45, .8)
            on_press:
                print(self.get_rgba)
                print(self.get_rgb)
                print(self.get_hsv)
                print(self.get_hex)
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
