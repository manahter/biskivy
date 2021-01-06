from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

import biskivy

Window.size = (500, 500)
Window.clearcolor = (.22, .22, .22, 1)

root = Builder.load_string("""
FloatLayout:
    BoxLayout:
        size_hint: .5, .5
        pos_hint: {"center_x": .5, "center_y": .5}
        
        BoxLayout:
            orientation: "vertical"

            #######################################################
            #################################### These are examples
            BisBoxLayout:
                size_hint: 1, 1
                canvas:
                    Color:
                        rgb: .5, .4, .3
                    Rectangle:
                        size: self.size
                        pos: self.pos
            BisDivider:
            BisBoxLayout:
                size_hint: 1, 1
                canvas:
                    Color:
                        rgb: .3, .5, .4
                    Rectangle:
                        size: self.size
                        pos: self.pos
            BisDivider:
            BisBoxLayout:
                size_hint: 1, 1
                canvas:
                    Color:
                        rgb: .8, .2, .4
                    Rectangle:
                        size: self.size
                        pos: self.pos
            #######################################################
            #######################################################
        
        BisDivider:
            
        BoxLayout:
            size_hint: 1, 1
            canvas:
                Color:
                    rgb: .4, .3, .5
                Rectangle:
                    size: self.size
                    pos: self.pos
            #######################################################
            #######################################################
        
        BisDivider:
        
        BoxLayout:
            size_hint: 1, 1
            canvas:
                Color:
                    rgb: .2, .5, .8
                Rectangle:
                    size: self.size
                    pos: self.pos
            #######################################################
            #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
