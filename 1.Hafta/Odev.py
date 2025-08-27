### Bölüm 1: Veri Tipleri ###

""" 1. Kullanicidan adini, yasini ve boyunu (float) input() ile aliniz. Bu bilgileri uygun veri
tiplerinde değişkenlerde saklayiniz ve ekrana anlamli bir şekilde yazdiriniz.
"""

# Name = input("İsminiz Nedir: ")
# Age = int(input("Yaşınız:"))
# Height = float(input("Boyunuz(metre cinsinden örn: 1.70):")) 

# print("Ben {0},{1} yaşındayım.Boyum {2:.2f} ".format(Name,Age,Height))



""" 2. Bir öğrencinin notlarını (Matematik, Fizik, Kimya) int tipinde değişkenlere atayın.
Ortalamasını float tipinde hesaplayıp ekrana yazdırınız.
"""
# Matematik = int(input("Matematik notunuz: "))
# Fizik = int(input("Fizik notunuz: "))
# Kimya = int(input("Kimya notunuz: "))
# Average = (Matematik + Fizik + Kimya) / 3
# print(f"Ortalamanız: {Average:.2f}")


"""3. Bir string değişkeni tanımlayın. Bu stringin ilk ve son karakterini, uzunluğunu ve ters
çevrilmiş halini ekrana yazdırınız"""

# Text = input("Metin giriniz: ")

# print(f"İlk karakter: {Text[0]}, Son karakter: {Text[-1]}, Uzunluk: {len(Text)}, Ters: {Text[::-1]}")



""" 4. Kullanıcıdan iki sayı alınız. Bu sayılar üzerinde toplama, çıkarma, çarpma, bölme ve mod
işlemleri yapınız.
"""

# FirstNum = int(input("İlk sayıyı giriniz:"))
# SecondNum = int(input("İkinci sayıyı giriniz (İkinci sayı sıfır olmamalı):"))

# print(f"{FirstNum} + {SecondNum } = {FirstNum+SecondNum }")
# print(f"{FirstNum} - {SecondNum } = {abs(FirstNum-SecondNum )}")
# print(f"{FirstNum} * {SecondNum } = {FirstNum*SecondNum }")
# print(f"{FirstNum} / {SecondNum} = {FirstNum/SecondNum}")   # if SecondNum is not equal zero
# print(f"{FirstNum} % {SecondNum } = {FirstNum%SecondNum }")



""" 5. Bir öğrencinin ortalaması 50’den büyükse 'Geçti', değilse 'Kaldı' çıktısını veren bir
program yazınız. (Karşılaştırma ve mantıksal operatörler kullanılacak.)"""

# Average = float(input("Öğrencinin ortalamasını giriniz: "))

# if Average > 50:
#     print("Geçti")
# else:
#     print("Kaldı")

""" 6. Kullanıcıdan yaşını alınız. Eğer yaş 18’den büyükse 'Ehliyet alabilirsiniz', değilse 'Ehliyet
alamazsınız' çıktısı veriniz."""

# Age = int(input("yaşınız:"))

# print("Ehliyet alabilirsiniz" if Age > 18 else "Ehliyet alamazsınız") ternary kullanımı


""" 7. Bir ürünün fiyatını (float) ve indirim oranını (yüzde) alınız. İndirimli fiyatı hesaplayıp
ekrana yazdırınız. (Aritmetik operatörler kullanılacak.)
"""

# Price = float(input("Ürünün fiyatı : "))
# DiscountRate = float(input("İndirim oranı (örn:%20 ): "))
# DiscountedPrice = Price * (1 - DiscountRate / 100)

# print(f"İndirimli fiyat: {DiscountedPrice:.2f} TL") float format


""" 8. True ve False değerlerini içeren değişkenlerle mantıksal operatörleri (and, or, not)
uygulayarak örnekler yapınız ve sonuçlarını ekrana yazdırınız."""

# Age = int(input("Yaşınız: "))
# IsStudent = input("Öğrenci misiniz? (evet/hayır): ").lower() == "evet"
# HasJob = input("İşiniz var mı? (evet/hayır): ").lower() == "evet"


# if Age > 18 and not IsStudent:
#     print("Yaşınız 18'den büyük ve öğrenci değilsiniz, işiniz vardır.")

# if not HasJob and Age > 18:
#     print("İşiniz yok ve yaşınız 18'den büyük, iş aramalısınız.")

# if Age < 18 or IsStudent:
#     print("Yaşınız 18'den küçük veya öğrenci olduğunuz için iş aramanıza gerek yok.")


