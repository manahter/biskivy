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
        
        BisSliderInput:
            prop_text: "Float"
            prop_min: 0
            prop_max: 2
            prop_value: 1.001
            prop_default: 0.5
            prop_unit: "mm"
            
        BisSliderInput:
            prop_text: "Int"
            prop_type: int
            prop_unit: "kg"
            prop_max: 10
            prop_step: 1
            prop_value: 7
            
        BisSliderInput:
            prop_unit: "ft"
            prop_type: int
            prop_max: 1000
            prop_step: 10
            prop_value: 300
            
        BisSliderInput:
            prop_text: "Disabled"
            disabled: True
            prop_value: .5
            
        BisCombinLayout:
            orientation: "horizontal"
            BisSliderInput:
                prop_value: .3
            BisSliderInput:
                prop_value: .5
            BisSliderInput:
                prop_value: .7
                
        BisCombinLayout:
            orientation: "vertical"
            BisSliderInput:
                prop_color: (1, .2, .45, .8)
                prop_value: .3
            BisSliderInput:
                prop_color: (1, .9, .6, .8)
                prop_value: .2
            BisSliderInput:
                prop_color: (.3, 1, .6, .8)
                prop_value: .1

        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
