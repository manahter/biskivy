"""
Register KivyMD widgets to use without import
"""

from kivy.factory import Factory

r = Factory.register
''' Layouts '''
r("BisWindow", module="biskivy.uix.window")
r("BisBoxLayout", module="biskivy.uix.boxlayout")
r("BisCombinLayout", module="biskivy.uix.combinlayout")
r("BisScrolledBoxLayout", module="biskivy.uix.scrolledlayout")

''' Labels '''
r("BisLabelAligned", module="biskivy.uix.label")
r("BisLabel", module="biskivy.uix.label")

''' Buttons '''
r("BisButton", module="biskivy.uix.button")
r("BisToggleButton", module="biskivy.uix.togglebutton")

''' Inputs '''
r("BisTextInput", module="biskivy.uix.textinput")
r("BisNumberInput", module="biskivy.uix.numberinput")
r("BisSliderInput", module="biskivy.uix.sliderinput")

''' Color Picker '''
r("BisColor", module="biskivy.uix.color")
r("BisColorWindow", module="biskivy.uix.color")
r("BisColorPicker", module="biskivy.uix.color")

''' Menu '''
r("BisMenu", module="biskivy.uix.menu")
r("BisMenuItem", module="biskivy.uix.menu")
r("BisMenuSeperator", module="biskivy.uix.menu")

r("BisSelectMenu", module="biskivy.uix.selectmenu")
r("BisSelectMenuItem", module="biskivy.uix.selectmenu")

''' '''
r("BisPanel", module="biskivy.uix.panel")
r("BisPanelItem", module="biskivy.uix.panel")


r("WiDrag", module="biskivy.uix.ortak.wi_drag")


r("BisIcon", module="biskivy.uix.icon")

r("BisDivider", module="biskivy.uix.divider")
