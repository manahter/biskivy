from kivy.uix.button import Button

from biskivy.uix.ortak.button import OrtakButton


class BisButton(Button, OrtakButton):
    """
    Bildiğimiz Button'un biraz daha özellik eklenmiş halidir.

    Kalıtılanlar:
        Button, HoverBehaviorS1, AvarS1Round

    Renkler
        renk_text: (.91, .91, .91, 1)
        renk_t_selected: (1, 1, 1, 1)
        renk_t_item: (1, 1, 1, 1)

        renk_inner: (.349,.349,.349,1)
        renk_selected: (.337,.502,.761,0.902)
        renk_outline: (.216,.216,.216,1)


    text: " "
        Butonda yazan yazı. Buton daraldıkça, bu yazı "..."
        şeklinde kısalır.

    prop_icon: ""
        Eğer prop_icon girilirse, butonun sol tarafına yerleşir
        Eğer text yoksa prop_icon, butona ortalanır

    prop_only_icon: False
        Eğer sadece prop_icon görünsün isteniyorsa True yapılır

    .. versionchanged:: 18.05.2020
        Verisyon takip tarihi eklendi

    """
