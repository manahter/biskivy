class WiARC:
    """
    Add,Remove,Clear_Widget

    .. versionchanged:: 18.05.2020
        Versiyon takip tarihi eklendi
    """

    wiarc_accepted_widgets = ()
    """Buradakiler self'e eklenir.
    kullanım:
        wiarc_accepted_widgets = (MyClass1, MyClass2, MyClass3)
    """

    wiarc_accepted_to_kasa = False
    """ 
    True  -> Widget, wiarc_accepted_widgets deki tiplerden ise kasaya ekle
    False -> Widget, wiarc_accepted_widgets deki tiplerden değil ise kasaya ekle
    """

    wiarc_widget_kasa = None
    """wiarc_accepted_widgets dışındakler, kasaya eklenir
    kullanım:
        wiarc_widget_kasa = self.ids.arcwkasa
    """

    wiarc_widget_sakla = []
    """Widget'i koyacak yer bulunamadıysa burada biriktirilir
    """

    def add_widget(self, widget, **kwargs):
        # def add_widget(self, widget, index=0, canvas=None):
        if isinstance(widget, self.wiarc_accepted_widgets) is not self.wiarc_accepted_to_kasa:
            super().add_widget(widget, **kwargs)
        else:
            if not self.wiarc_widget_kasa and self.ids.arcwkasa:
                self.wiarc_widget_kasa = self.ids.arcwkasa
            self.wiarc_widget_kasa.add_widget(widget, **kwargs)

    def remove_widget(self, widget):
        if isinstance(widget, self.wiarc_accepted_widgets):
            super().remove_widget(widget)
        else:
            if not self.wiarc_widget_kasa and self.ids.arcwkasa:
                self.wiarc_widget_kasa = self.ids.arcwkasa
            self.wiarc_widget_kasa.remove_widget(widget)

    def clear_widgets(self, children=None):
        if isinstance(children, self.wiarc_accepted_widgets):
            super().clear_widgets(children)
        else:
            if not self.wiarc_widget_kasa and self.ids.arcwkasa:
                self.wiarc_widget_kasa = self.ids.arcwkasa
            self.wiarc_widget_kasa.clear_widgets(children=children)

