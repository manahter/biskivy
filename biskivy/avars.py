"""
Widget'ler için şunları sağlar;
    * Ortak Değişkenler
    * Yardımcı Ortak Değişkenler
"""

from kivy.lang import Builder

Builder.load_string("""
<AvarS1Round>:
    ###################### Köşe yuvarlama - ROUND
    # Eğer kalıtılan widget'ın scale_round değişkeni yoksa diye tanımlandı..
    scale_round: 0
    #capi: self.scale_round * bkv.prefs.scale.roundkats if self.scale_round * bkv.prefs.scale.roundkats < self.height/2 else self.height/2
    capi: self.scale_round * (self.height / 2)

    tek: True       # 1 -> Tek mi?,  0 -> Grup halinde mi?
    bas: False      # 1 -> Başta,    0 -> Başta değil
    son: False      # 1 -> Sonda,    0 -> Sonda değil
    yat: False      # 1 -> Yatay,    0 -> Değil
    dik: False      # 1 -> Dikey,    0 -> Değil

    solu: self.capi if self.tek or self.bas else 0
    sagu: self.capi if self.tek or (self.yat and self.son) or (self.dik and self.bas) else 0
    saga: self.capi if self.son or self.tek else 0
    sola: self.capi if self.tek or (self.yat and self.bas) or (self.dik and self.son) else 0
    kose_dizi: [self.solu, self.sagu, self.saga, self.sola]
    #####################################

""")


class AvarS1Round:
    """Variables. Köşe yuvarlaklık değişkenleri"""
    pass
