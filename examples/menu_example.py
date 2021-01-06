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
        BisMenu:
            prop_text: "This is a BisMenu"
            prop_width: 200
            prop_align: "auto"
            
            BisMenuItem:
                prop_text: "Bool Tool"
                prop_hint: "Shift Ctrl B"
                prop_icon: "./biskivy/images/damlalik.png"
                BisMenuItem:
                    prop_text: "Difference"
                    prop_hint: "Shift Ctrl Numpad -"
                    prop_icon: "./biskivy/images/damlalik.png"
                BisMenuItem:
                    prop_text: "Union"
                    prop_hint: "Shift Ctrl Numpad +"
                BisMenuItem:
                    prop_text: "Intersect"
                    prop_hint: "Shift Ctrl Numpad *"
                BisMenuItem:
                    prop_text: "Slice"
                    prop_hint: "Shift Ctrl Numpad /"
            
            BisMenuItem:
                prop_text: "Delete Global"
                
            BisMenuItem:
                prop_text: "Delete"
                
            BisMenuSeperator:
            
            BisMenuItem:
                prop_text: "Show/Hide"
                BisMenuItem:
                    prop_text: "Show Hidden Objects"
                    prop_hint: "Alt H"
                BisMenuItem:
                    prop_text: "Hide Selected"
                    prop_hint: "H"
                BisMenuItem:
                    prop_text: "Hide Unelected"
                    prop_hint: "Shift H"
                
            BisMenuSeperator:
            
            BisMenuItem:
                prop_text: "Convert to"
                
            BisMenuSeperator:
            
            BisMenuItem:
                prop_text: "Quick Effects"
                
            BisMenuSeperator:
            
            BisMenuItem:
                prop_text: "Rigid Body"
                BisColor:
                
            BisMenuItem:
                prop_text: "Animation"
                BisMenuItem:
                    prop_text: "Object"
                    BisMenuItem:
                        prop_text: "Cube"
                    BisMenuItem:
                        prop_text: "Sphere"
                    BisMenuItem:
                        prop_text: "Plane"
                BisMenuItem:
                    prop_text: "Path"
                    BisMenuItem:
                        prop_text: "Curve"
                    BisMenuItem:
                        prop_text: "Bezier"
                    BisMenuItem:
                        prop_text: "Path"
            BisMenuSeperator:
            
            BisMenuItem:
                prop_text: "Shade Flat"
                
            BisMenuItem:
                prop_text: "Shade Smooth"
        
        BisCombinLayout:
                 
            BisMenu:
                prop_text: "Combine"
                prop_width: 200
                prop_align: "auto"
                BisMenuItem:
                    prop_text: "Item 1"
                BisMenuItem:
                    prop_text: "Item 2"
                BisMenuItem:
                    prop_text: "Item 3"
            BisMenu:
                prop_text: "Menu"
                prop_width: 200
                prop_align: "auto"
                BisMenuItem:
                    prop_text: "Item 1"
                BisMenuItem:
                    prop_text: "Item 2"
                BisMenuItem:
                    prop_text: "Item 3"
                    prop_bind: lambda: print(self.prop_text)
                
        BisSelectMenu:
            prop_title: "Select Menu"
            prop_width: 200
            prop_align: "auto"
            
            prop_items: [{"prop_text": "Object Mode", "prop_icon":bkv.paths.icons.locked},\
                {"prop_text": "Edit Mode"},\
                {"prop_text": "Sculpt Mode"},\
                {"prop_text": "Vertex Mode", "prop_bind": lambda *args: print("Vertex", args)},\
                {"prop_text": "Weight Mode"},\
                {"prop_text": "Texture Mode", "prop_hint": "Ctrl Shift Space"},\
                ]
        #######################################################
        #######################################################
""")


class Apim(App):
    def build(self):
        return root


if __name__ == "__main__":
    Apim().run()
