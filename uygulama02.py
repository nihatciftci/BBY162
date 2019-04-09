"""
NİHAT FURKAN ÇİFTÇİ
TEST UYGULAMASI
09/04/2019
"""
print("~~~~BASİT GENEL KÜLTÜR TESİ~~~~")
print("LÜTFEN SORULARI DİKKATLİ OKUYUNUZ, HER DOĞRU CEVAP 20 PUAN KAZANDIRIR")
#SORULAR
sorular = ["Mısır piramidlerinden hangisi en büyüktür?",\
            "Aşağıdakilerden hangisi Kanada\'nın resmi dillerinden birisidir?",\
            "Avrupa Birliği\'nin başkenti neresidir?",\
            "İtalya\'da bulunan her 100 yılda bir yere 7 cm yaklaşan Pisa Kulesi hangi yöne doğru eğilmektedir?",\
            "Atatürk Havalimanın\'dan son resmi uçuş nereye yapılmıştır?"]

#CEVAPLAR
cevaplar = ["A","C","A","B","C"]

#ŞIKLAR
sıklar_A = ["Kefren Piramidi" ,"İtalyanca", "Brüksel", "Kuzey", "New York"]
sıklar_B = ["Sfenks Piramidi", "Almanca", "Lüksemburg", "Güney", "Bükreş"]
sıklar_C = ["Mikerinos Piramidi", "Fransızca", "Berlin", "Batı", "Singapur"]
puan = 0

#TEST
for i in range(len(sorular)):
    print("Soru "+str(i+1)+":"+sorular[i])
    print("A) " + sıklar_A[i])
    print("B) " + sıklar_B[i])
    print("C) " + sıklar_C[i])
    cevap = input("CEVABINIZI GİRİN :")
    if(cevaplar[i] == cevap.upper()):
        print("TEBRİKLER, DOĞRU CEVAP!")
        print("SONRAKİ SORUYA GEÇİNİZ!")
        puan +=20
    else:
        print("CEVABINIZ YANLIŞ!")
        print("SONRAKİ SORUYA GEÇİNİZ!")

#PUANLAMA
print("------------------------------------------------------------------------------------")
print ("TEBRİKLER SINAVI TAMAMLADINIZ!""ALDIĞINIZ PUAN: "+str(puan))
print("------------------------------------------------------------------------------------")
if puan <=60:
    print("MAALESEF PUANINIZ ORTALAMANIN ALTINDA,DAHA SONRA TEKRAR DENEYİN")
else:
    print("TEBRİKLER ORTALAMANIN ÜSTÜNDESİNİZ")

sayı = input("LÜTFEN TESTİMİZİ 1-10 ARASINDA DEĞERLENDİRİNİZ =")
print("------------------------------------------------------------------------------------")
print("VERMİŞ OLDUĞUNUZ PUAN",sayı,"ANKETİMİZE KATILDIĞINIZ İÇİN TEŞEKKÜR EDERİZ")
print("------------------------------------------------------------------------------------")