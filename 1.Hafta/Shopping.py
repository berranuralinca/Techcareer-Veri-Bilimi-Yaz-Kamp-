""" 9. Küçük bir alışveriş sepeti uygulaması yapınız:
- Kullanıcıdan 3 ürünün fiyatını alınız.
- Toplam fiyatı hesaplayınız.
- Eğer toplam fiyat 200 TL’den fazlaysa %10 indirim uygulayınız.
- Son fiyatı ekrana yazdırınız."""


Price1 = float(input("İlk ürün fiyatı: "))
Price2 = float(input("İkinci ürün fiyatı: "))
Price3 = float(input("Üçüncü ürün fiyatı: "))
DiscountRate = 10

TotalPrice = Price1 + Price2 + Price3

if TotalPrice > 200:
    print("İndirimli fiyat : " ,TotalPrice * (1 - DiscountRate / 100))
else:
    print("Toplam fiyat:",TotalPrice)

