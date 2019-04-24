#soru1
metin = ("Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır.")
slices = metin[:20]
print(slices)

#soru2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:
    print(i)

#soru3
sozluk = {"elma" : "Ağaçta yetişen bir tür meyve" , "salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
giris = input("aramak istediğiniz kelimeyi giriniz")
giris == giris.lower()
while True:
    if giris == "elma":
        print(sozluk["elma"])
        break
    elif giris == "salatalık":
        print(sozluk["salatalık"])
        break
    else:
        print("yanlış giriş")
        break

