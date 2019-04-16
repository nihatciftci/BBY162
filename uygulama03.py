"""
NİHAT FURKAN ÇİFTÇİ
16/04/2019
ADAM ASMACA ÇALIŞMASI
"""
print("~~~~Adam Asmaca Oyunu~~~~")
print("Her kelime için 7 tahmin hakkınız vardır !")
print("-------------------BOL ŞANSLAR--------------------")

import random
AdamAsmaca = ("<3<3<3<3<3<3<3","<3<3<3<3<3<3","<3<3<3<3<3","<3<3<3<3","<3<3<3","<3<3","<3")
maxcan = len(AdamAsmaca) - 1
kelimeler = ("türkiye","amerika","almanya","portekiz","azerbaycan","suriye",
             "kanada","brezilya","arjantin","mısır","japonya","çin",
             "rusya","senegal","fas","kuveyt","ingiltere","ispanya","fransa")
secilen = random.choice(kelimeler)
rastgele = "-" * len(secilen)
can = 0
girilen = []


while can <= maxcan and rastgele !=secilen:
    print(AdamAsmaca[can])
    print("Girdiğiniz harfler : ", girilen )
    print("Bilmeniz gereken kelime : ", rastgele)
    print("Kalan hakkınız : ", 7-can)
    tahmin = input("\nHarf giriniz: ").lower()

    while tahmin in girilen:
        print("Bu harfi zaten kullandınız")
        tahmin = input("\nHarf giriniz: ").lower()
    girilen.append(tahmin)
    if tahmin in secilen:
        print("Tebrikler ! Doğru tahmin ettiniz")
        yeni = ""
        for i in range(len(secilen)):
            if tahmin == secilen[i]:
                yeni += tahmin
            else:
                yeni += rastgele[i]
        rastgele = yeni
    else:
        print("Yanlış tahmin tekrar deneyiniz.")
        can += 1
if can > maxcan:
    print("Tüm haklarınızı bitirdiniz oyuna tekrar başlayın.")
    print("Cevap: ", secilen)
else:
    print("Tebrikler, yeni kelimeye geçebilirsiniz.")
    print("Cevap: ", secilen)

sayı = input("LÜTFEN TESTİMİZİ 1-10 ARASINDA DEĞERLENDİRİNİZ =")
print("------------------------------------------------------------------------------------")
print("VERMİŞ OLDUĞUNUZ PUAN",sayı,"ANKETİMİZE KATILDIĞINIZ İÇİN TEŞEKKÜR EDERİZ")
print("------------------------------------------------------------------------------------")