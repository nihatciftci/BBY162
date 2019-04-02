"""
Test uygulaması = uygulama01
NİHAT FURKAN ÇİFTÇİ 31/03/2019
"""

print("~~~~Kolay Matematik Testi~~~~")
print("Lütfen size doğru gelen şıkkı yazarak cevaplayınız")
sorular = ["4*4 A)16 B)8 C)12 = ", "3*3 A)13 B)9 C)15 =", "7*7 A)44 B)47 C)49 =", "9*9 A)81 B)88 C)78 =", "5*5 A)10 B)15 C)25 ="]
cevaplar = ["A","B","C","A","C"]
puan = 0
#soru1
cevap = input((sorular[0]))
if cevaplar[0] == cevap.upper():
    print("Tebrikler, doğru bildiniz!")
    puan +=1
else:
    print("Cevabınız yanlış!")
#soru2
cevap = input((sorular[1]))
if cevaplar[1] == cevap.upper():
    print("Tebrikler, doğru bildiniz!")
    puan +=1
else:
    print("Cevabınız yanlış!")
#soru3
cevap = input((sorular[2]))
if cevaplar[2] == cevap.upper():
    print("Tebrikler, doğru bildiniz!")
    puan +=1
else:
    print("Cevabınız yanlış!")
#soru4
cevap = input((sorular[3]))
if cevaplar[3] == cevap.upper():
    print("Tebrikler, doğru bildiniz!")
    puan +=1
else:
    print("Cevabınız yanlış!")
#soru5
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
    print("Tebrikler, doğru bildiniz!")
    puan +=1
    print("Tebrikler sınavı tamamladınız!""puanınız :" + str(puan * 20))
else:
    print("Cevabınız yanlış!")
    print("Tebrikler sınavı tamamladınız!""puanınız :" + str(puan * 20))


sayı = input("Lütfen testimizi 1-10 arasında değerlendiriniz =")
print("Vermiş olduğunuz puan",sayı,"anketimize katıldığınız için teşekkür ederiz")