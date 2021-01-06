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
        BisNumberInput:
            prop_text: "Float"
            prop_min: 0
            prop_max: 2
            prop_step: 0.01
            prop_value: 1.001
            prop_default: 0.5
            prop_unit: "mm"
                    
        BisNumberInput:
            prop_text: "Int"
            prop_type: int
            prop_unit: "kg"
        
        BisNumberInput:
            prop_value: 321.012
            prop_unit: "ft"
            
        BisNumberInput:
            prop_text: "Disabled"
            disabled: True
            
        BisCombinLayout:
            orientation: "horizontal"
            BisNumberInput:
                prop_type: int
                prop_value: 1
            BisNumberInput:
                prop_type: int
                prop_value: 2.5
            BisNumberInput:
                prop_type: int
                prop_value: 3.32
                
        BisCombinLayout:
            orientation: "vertical"
            BisNumberInput:
                prop_type: int
                prop_value: 123
            BisNumberInput:
                prop_type: int
                prop_value: 456
            BisNumberInput:
                prop_type: int
                prop_value: 789
        
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
