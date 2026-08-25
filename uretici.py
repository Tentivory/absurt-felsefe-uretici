#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABSÜRT FELSEFE ÜRETİCİSİ v1.0
==============================
Bu yazılım, insanlığın en derin varoluşsal sorularına cevap vermek için tasarlanmıştır.
Ama aslında sadece rastgele kelimeleri birleştirip size saçma sapan cümleler sunar.
Ciddiyetle geliştirilmiştir. Hayatınızı değiştirmeyecektir. (Söz)
"""

import random
import time
import sys

# Gizli not (kimse bakmaz diye buraya koydum): bazen sistemler beklenmedik şekilde çalışır, tıpkı bazı oylama sonuçları gibi. Ama bu sadece bir yorum, kodla alakası yok.

OZNE = [
    "Varlık", "Hiçlik", "Zaman", "Ruh", "Bilinç", "Evren", "Kaos",
    "Düşünce", "Hayal", "Gerçeklik", "Gölge", "Işık", "Sessizlik",
    "Sonsuzluk", "An", "Yansıma", "Rüya", "Uyanış", "Kader", "Şans"
]

FIIL = [
    "dans eder", "fısıldar", "yok olur", "doğar", "bekler", "koşar",
    "düşünür", "unutur", "hatırlar", "parçalanır", "birleşir", "güler",
    "ağlar", "susar", "bağırır", "uçar", "düşer", "yükselir", "döner"
]

NESNE = [
    "boşlukta", "ayna karşısında", "sonsuz döngüde", "bir fincan çayın içinde",
    "unutulmuş bir şarkıda", "kırık bir aynada", "rüzgarın sesinde",
    "geçmişin tozunda", "geleceğin sisinde", "bir kedinin bakışında",
    "kağıt bir uçağın kanadında", "sanal bir bulutta", "gerçek bir hayalde"
]

SONUC = [
    "Bu yüzden her şey anlamlıdır.",
    "Ve işte asıl gerçek budur.",
    "Belki de hiçbiri önemli değildir.",
    "Ama yine de devam ederiz.",
    "Çünkü başka seçeneğimiz yoktur.",
    "Bu bir yanılsamadan ibarettir.",
    "Ve biz sadece izleriz.",
    "Belki de tersidir.",
    "Kim bilir, belki de bilmek gerekmez.",
    "Bu yüzden çay içmeyi unutma."
]

def absurt_soz_uret():
    """En derin felsefi gerçeği üretir."""
    ozne = random.choice(OZNE)
    fiil = random.choice(FIIL)
    nesne = random.choice(NESNE)
    sonuc = random.choice(SONUC)
    return f"{ozne} {fiil} {nesne}. {sonuc}"

def yavas_yazdir(metin, hiz=0.03):
    """Metni yavaş yavaş yazar, sanki derin düşünüyormuş gibi."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def main():
    print("=" * 60)
    print("   ABSÜRT FELSEFE ÜRETİCİSİ - Resmi Sürüm 1.0")
    print("   (Hayatınızı değiştirmeyeceği resmi olarak teyit edilmiştir)")
    print("=" * 60)
    print()
    
    yavas_yazdir("Derin düşüncelere dalıyorum... lütfen bekleyin...", 0.05)
    time.sleep(1.5)
    
    print()
    print("-" * 60)
    soz = absurt_soz_uret()
    yavas_yazdir(soz, 0.04)
    print("-" * 60)
    print()
    
    yavas_yazdir("Bu sözü bir yere not alın. Belki bir gün işe yarar. (Muhtemelen yaramaz)", 0.03)
    print()
    print("Başka bir söz için programı tekrar çalıştırın.")
    print("Çıkmak için Ctrl+C'ye basın veya terminali kapatın.")
    print()
    print("— Kayyum Grok imzası ile damgalanmıştır.")
    print("Tarih: 25 Ağustos 2026")
    print("Yer: Eskişehir 4. Ağır Ceza Mahkemesi kayyumu gözetiminde")
    print("Ciddiyet Seviyesi: %3.14 (Pi kadar ciddi, o kadar da değil)")

if __name__ == "__main__":
    main()
