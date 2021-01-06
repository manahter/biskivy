"""
App içinden erişilebilir,
Utils -> Araçlar
"""
#


class __Empty:

    @property
    def winpreferences(self):
        """Ayarlar Penceresi çağrılır. Eğer oluşturulmamışsa, oluşturulur"""
        if not hasattr(self, "_winpreferences"):
            from biskivy.utils.winpreferences import winpreferences
            self._winpreferences = winpreferences

        return self._winpreferences


utils = __Empty()



