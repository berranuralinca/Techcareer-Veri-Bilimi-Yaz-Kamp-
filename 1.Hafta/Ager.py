import datetime

""" 10. Kullanıcıdan doğum yılını alınız. Bu yıl ile güncel yılı kullanarak yaşını hesaplayınız.
Yaşına göre şu mesajlardan birini veriniz:
- 0-12: 'Çocuksunuz'
- 13-17: 'Ergensiniz'
- 18 ve üzeri: 'Yetişkinsiniz'
"""

BirthDate =int(input("Doğum yılınız: "))

Age  = datetime.datetime.now().year-BirthDate

if Age <= 12:
    print("Çocuksunuz")
elif Age <= 17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")