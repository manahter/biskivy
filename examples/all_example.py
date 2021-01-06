from kivy.core.window import Window
#Window.borderless = True
from kivy.app import App
import biskivy

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Window.size = (900, 600)
Window.clearcolor = (.22, .22, .22, 1)
#indow.set_icon(bkv.paths.icons.ucnokta.png")
#indow.icon = bkv.paths.icons.ucnokta.png"


root = Builder.load_string("""
<Ana>:
    BoxLayout:
        orientation: "horizontal"
        GridLayout            
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            size_hint: 2, None
            
        BisDivider:
        
        BisPanel:
            orientation: "vertical"
            ##########
            BisPanelItem:
                prop_title: "BisLabel"
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
            
            ##########
            BisPanelItem:
                prop_title: "BisButton"
                BisButton:
                    prop_text: "Text BisButton"
                    on_press: 
                        print(bkv.prefs.button.renk_selected)
                        #app.prefs.button.aha["a"]["b"] = 5
                        #app.prefs.button.renk_selected = [0.7, 0.503, 0.561, 0.902]
                BisButton:
                    prop_text: "Text + Icon BisButton"
                    #prop_text: bkv.prefs.button.name
                    prop_icon: bkv.paths.icons.menu
                        
                BisPanelItem:
                    prop_title: "BisButton"
                    BisButton:
                        prop_text: "Text BisButton"
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
            
            ##########
            BisPanelItem:
                prop_title: "BisToggleButton"
                
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
            
            BisPanelItem:
                prop_title: "BisNumberInput"
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
                        
            BisPanelItem:
                prop_title: "BisSliderInput"
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
                
            
            BisPanelItem:
                prop_title: "BisTextInput"
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
                
                    
            BisPanelItem:
                prop_title: "BisColor -> Windowed Color Picker"
                BoxLayout: 
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: 5
                    BisLabelAligned:
                        prop_text: "Single"
                    BisColor:
                        hex: "#72FFFFCC"
                        
                BoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: 5
                    BoxLayout:
                        orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Combine"
                        BisLabelAligned:
                            prop_text: "Color Picker"
                        BisLabelAligned:
                            prop_text: "RGB / HSV / Hex"
                    BisCombinLayout:
                        orientation: "vertical"
                        BisColor:
                            prop_title: "Renk Seç"
                            rgb: (1, .9, .6)
                        BisColor:
                            hsv: (.4, .7, 1)
                        BisColor:
                            rgba: (1, .2, .45, .8)
                            on_press:
                                print(self.get_rgba)
                                print(self.get_rgb)
                                print(self.get_hsv)
                                print(self.get_hex)
                                
            BisPanelItem:
                prop_title: "BisMenu -> Windowed Collapsible Menu"
                collapse: False
                #orientation: "horizontal"
                
                BisMenu:
                    prop_text: "This is a BisMenu"
                    prop_width: 200
                    prop_align: "auto"
                    
                    BisMenuItem:
                        prop_text: "Bool Tool"
                        prop_hint: "Shift Ctrl B"
                        prop_icon: bkv.paths.icons.damlalik
                        BisMenuItem:
                            prop_text: "Difference"
                            prop_hint: "Shift Ctrl Numpad -"
                            prop_icon: bkv.paths.icons.damlalik
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
                    
                    prop_items: [{"prop_text": "Object Mode", "prop_icon": bkv.paths.icons.locked},\
                        {"prop_text": "Edit Mode"},\
                        {"prop_text": "Sculpt Mode"},\
                        {"prop_text": "Vertex Mode", "prop_bind": lambda *args: print("Vertex", args)},\
                        {"prop_text": "Weight Mode"},\
                        {"prop_text": "Texture Mode", "prop_hint": "Ctrl Shift Space"},\
                        ]
                    # , "prop_select":True
                    
            BisPanelItem:
                prop_title: "Preferences Window"
                collapse: False
                #orientation: "horizontal"
                BisButton:
                    prop_text: "Preferences Window"
                    on_press:
                        bkv.utils.winpreferences.toggle()
""")


class Ana(BoxLayout):
    pass


class Apim(App):
    def build(self):
        return Ana()


if __name__ == "__main__":
    Apim().run()
