from kivy.lang import Builder

from biskivy.uix.panel import BisPanel

Builder.load_string("""
<BisWinPrefThemes>:
    orientation: "vertical"
    BisPanelItem:
        prop_title: "User Interface"
        prop_padding: [0,]
        
        ### LABEL
        BisMenuItem:
            prop_text: "Label"
            prop_orientation: "horizontal"
            prop_padding: [10,]
            prop_spacing: 10
            
            BisBoxLayout:
                prop_orientation: "vertical"
                spacing: 5
                BisBoxLayout:
                    spacing: 5
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Text"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Item"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.label.renk_text
                            on_get_rgba:
                                bkv.prefs.label.renk_text = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.label.renk_t_selected
                            on_get_rgba:
                                bkv.prefs.label.renk_t_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.label.renk_t_item
                            on_get_rgba:
                                bkv.prefs.label.renk_t_item = self.get_rgba
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Inner"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Outline"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.label.renk_inner
                            on_get_rgba:
                                bkv.prefs.label.renk_inner = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.label.renk_selected
                            on_get_rgba:
                                bkv.prefs.label.renk_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.label.renk_outline
                            on_get_rgba:
                                bkv.prefs.label.renk_outline = self.get_rgba
                    
        ### BUTTON
        BisMenuItem:
            prop_text: "Button"
            prop_orientation: "horizontal"
            prop_padding: [10,]
            prop_spacing: 10
            
            BisBoxLayout:
                prop_orientation: "vertical"
                spacing: 5
                BisBoxLayout:
                    spacing: 5
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Text"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Item"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.button.renk_text
                            on_get_rgba:
                                bkv.prefs.button.renk_text = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.button.renk_t_selected
                            on_get_rgba:
                                bkv.prefs.button.renk_t_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.button.renk_t_item
                            on_get_rgba:
                                bkv.prefs.button.renk_t_item = self.get_rgba
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Inner"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Outline"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.button.renk_inner
                            on_get_rgba:
                                bkv.prefs.button.renk_inner = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.button.renk_selected
                            on_get_rgba:
                                bkv.prefs.button.renk_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.button.renk_outline
                            on_get_rgba:
                                bkv.prefs.button.renk_outline = self.get_rgba
                       
                BisBoxLayout:
                    #spacing: 5
                    BisLabelAligned:
                        prop_text: "Roundness"
                    BisSliderInput:
                        size_hint_x: 3
                        prop_min: 0
                        prop_max: 1
                        prop_step: 0.001
                        prop_value: bkv.prefs.button.scale_round
                        on_prop_value: 
                            bkv.prefs.button.scale_round = round(self.prop_value, 3)
                        
        ### INPUT
        BisMenuItem:
            prop_text: "Input"
            prop_orientation: "horizontal"
            prop_padding: [10,]
            prop_spacing: 10
            
            BisBoxLayout:
                prop_orientation: "vertical"
                spacing: 5
                BisBoxLayout:
                    spacing: 5
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Text"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Item"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.input.renk_text
                            on_get_rgba:
                                bkv.prefs.input.renk_text = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.input.renk_t_selected
                            on_get_rgba:
                                bkv.prefs.input.renk_t_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.input.renk_t_item
                            on_get_rgba:
                                bkv.prefs.input.renk_t_item = self.get_rgba
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Inner"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Outline"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.input.renk_inner
                            on_get_rgba:
                                bkv.prefs.input.renk_inner = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.input.renk_selected
                            on_get_rgba:
                                bkv.prefs.input.renk_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.input.renk_outline
                            on_get_rgba:
                                bkv.prefs.input.renk_outline = self.get_rgba
                       
                BisBoxLayout:
                    #spacing: 5
                    BisLabelAligned:
                        prop_text: "Roundness"
                    BisSliderInput:
                        size_hint_x: 3
                        prop_min: 0
                        prop_max: 1
                        prop_step: 0.001
                        prop_value: bkv.prefs.input.scale_round
                        on_prop_value: 
                            bkv.prefs.input.scale_round = round(self.prop_value, 3)
                        
        ### TEXT INPUT
        BisMenuItem:
            prop_text: "Text Input"
            prop_orientation: "horizontal"
            prop_padding: [10,]
            prop_spacing: 10
            
            BisBoxLayout:
                prop_orientation: "vertical"
                spacing: 5
                BisBoxLayout:
                    spacing: 5
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Text"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Item"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_text
                            on_get_rgba:
                                bkv.prefs.textinput.renk_text = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_t_selected
                            on_get_rgba:
                                bkv.prefs.textinput.renk_t_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_t_item
                            on_get_rgba:
                                bkv.prefs.textinput.renk_t_item = self.get_rgba
                    BisBoxLayout:
                        prop_orientation: "vertical"
                        BisLabelAligned:
                            prop_text: "Inner"
                        BisLabelAligned:
                            prop_text: "Selected"
                        BisLabelAligned:
                            prop_text: "Outline"
                    BisCombinLayout:
                        prop_orientation: "vertical"
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_inner
                            on_get_rgba:
                                bkv.prefs.textinput.renk_inner = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_selected
                            on_get_rgba:
                                bkv.prefs.textinput.renk_selected = self.get_rgba
                        BisColor:
                            rgba: bkv.prefs.textinput.renk_outline
                            on_get_rgba:
                                bkv.prefs.textinput.renk_outline = self.get_rgba
                       
                BisBoxLayout:
                    #spacing: 5
                    BisLabelAligned:
                        prop_text: "Roundness"
                    BisSliderInput:
                        size_hint_x: 3
                        prop_min: 0
                        prop_max: 1
                        prop_step: 0.001
                        prop_value: bkv.prefs.textinput.scale_round
                        on_prop_value: 
                            bkv.prefs.textinput.scale_round = round(self.prop_value, 3)
                         
        ### COLOR
        BisMenuItem:
            prop_text: "Color"
            prop_orientation: "horizontal"
            prop_padding: [10,]
            prop_spacing: 10
            BisBoxLayout:
                #spacing: 5
                BisLabelAligned:
                    prop_text: "Roundness"
                BisSliderInput:
                    size_hint_x: 3
                    prop_min: 0
                    prop_max: 1
                    prop_step: 0.001
                    prop_value: bkv.prefs.color.scale_round
                    on_prop_value: 
                        bkv.prefs.color.scale_round = round(self.prop_value, 3)
              
""")


class BisWinPrefThemes(BisPanel):
    pass