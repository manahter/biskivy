from kivy.lang import Builder
from biskivy.uix.window import BisWindow
from biskivy.utils.winpreferences.interface import BisWinPrefInterfaces
from biskivy.utils.winpreferences.themes import BisWinPrefThemes


"""
BisWinPreferences
    Ayarları barındıran Penceredir.
    Mesela, buton, label vb. renkleri, boyutları vs'sini barındırır
    
"""


Builder.load_string("""
<BisWinPreferences>:
    id: winpref
    prop_title: "Biskivy Preferences"
    prop_orientation: "horizontal"
    
    prop_bgcolor_kasa: .259, .259, .259, 1
    
    on_open:
        self.ids.pinned.state = "down"
    
    BisScrolledBoxLayout:
        orientation: "vertical"
        padding: 10,
        spacing: 10
        size_hint_x: .3
        
        canvas.before:
            Color:
                rgba: .294, .294, .294, 1
            Rectangle:
                pos: self.pos
                size: self.size
                
        BisCombinLayout:
            orientation: "vertical"
            
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Interface"
                state: 'down'
                on_parent:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Themes"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Viewport"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Lights"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Editing"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Animations"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
                
        BisToggleButton:
            group: "winpreferences"
            prop_text: "Add-ons"
            on_state:
                if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            
        BisCombinLayout:
            orientation: "vertical"
            
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Input"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Navigation"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "KeyMap"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
                
        BisCombinLayout:
            orientation: "vertical"
            
            BisToggleButton:
                group: "winpreferences"
                prop_text: "System"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "Save & Load"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            BisToggleButton:
                group: "winpreferences"
                prop_text: "File Paths"
                on_state:
                    if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
        
        BisToggleButton:
            group: "winpreferences"
            prop_text: "Experimental"
            on_state:
                if self.state == "down": winpref.kasa_degis(self.prop_text)
                    
            
    BisDivider:
        
        
    BisBoxLayout:
        id: kasa
        size_hint: .7, 1
        orientation: "vertical"
        #padding: 0, 10, 10, 10
        #spacing: 10
        
""")


class BisWinPreferences(BisWindow):

    kasa_liste = {"Interface": BisWinPrefInterfaces(),
                  "Themes": BisWinPrefThemes(),
                  }

    def kasa_degis(self, module_name):
        self.ids.kasa.clear_widgets()
        kasa = self.kasa_liste.get(module_name, None)
        if kasa:
            self.ids.kasa.add_widget(kasa)


winpreferences = BisWinPreferences()
winpreferences.prop_spacing = 0
winpreferences.prop_padding = 0, 0, 0, 0
winpreferences.prop_width = 400
winpreferences.prop_height = 400
