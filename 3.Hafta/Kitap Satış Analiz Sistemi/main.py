import functions
import utils as ut
import analysis as a
from data import books
import train_test as tt

# Proje – “Kitap Satış Analiz Sistemi”

# Beklenen Çıktı Örneği
# • En çok satan kitap: "Makine Öğrenmesi"
# • Yazar satışları: {"Ali": 3400, "Ayşe": 1550, "Can": 1800, "Deniz": 400}
# • Türler: {"Bilim", "Akademik", "Sanat", "Sosyal"}
# • 1000’den fazla satan kitaplar: ["Veri Bilimi 101", "Makine Öğrenmesi","Matematiksel Modelleme"]
# • Ortalama satış: 1021.4
# • Standart sapma: ~480.2
# • Eğitim/ Test ayırımı sonrası analiz:

# Analizde Sizden Beklenen:
# • Veriyi uygun oranlarda ayırın (örneğin %70 train, %30 test).
# • Train seti üzerinde basit analizler yapın (ortalama, sıklık, vs.).
# • Test seti üzerinde aynı analizleri tekrarlayın.
# • Sonuçları karşılaştırın ve kısa yorum ekleyin.

author_avg,bigger_than,train_df,test_df = tt.train_test(books)

print("*********************************************************")
print("\n")
print("                  Kitap Satiş Analiz Sistemi             ")
print("\n")
print("*********************************************************")

print("---------------------------------------------------------")
print("   En çok satan kitap:",functions.most_popular_book(books))
print("---------------------------------------------------------")
print("Yazar satişlari:",functions.sales_author(books))
print("---------------------------------------------------------")
print("Türler:",ut.book_types(books))
print("---------------------------------------------------------")
print("1000'den fazla satan kitaplar:",ut.most_popular(books))
print("---------------------------------------------------------")
print("2020'den sonra çikan kitaplar:",ut.filter_year(books))
print("---------------------------------------------------------")
print("Satiş adetleri %10 arttirilmiş:",ut.sales_count(books))
print("---------------------------------------------------------")
print("Satiş miktarına göre azalan:",ut.sorted_sales(books))
print("---------------------------------------------------------")
print("*********************************************************")
print("                      İstatistikler                      ")
print("*********************************************************")
print("Ortalama satiş:",a.average_sales(books))
print("---------------------------------------------------------")
print("En çok satiş yapan tür:",a.popular_type(books))
print("---------------------------------------------------------")
print("Standart sapma:",a.std_dev(books))
print("---------------------------------------------------------")
print("*********************************************************")
print("                   Train/Test Simülasyonu:               ")
print("*********************************************************")
print("---------------------------------------------------------")
print("         Eğitim Seti: Yazarlarin Ortalama Satişlari      ")
print(author_avg, "\n")
print("---------------------------------------------------------")
print("  Test Setinde Ortalamanin Üzerinde Satiş Yapan Kitaplar ")
print(bigger_than[["name", "author", "sales", "author_average"]])
print("*********************************************************")
print("---------------------------------------------------------")
print("                      Train Set Analizi                  ")
print(train_df.describe().T)
print("---------------------------------------------------------")
for col in ['author', 'type', 'year']:
    print(f"\nSütun: {col}")
    print(train_df[col].value_counts())
    print("---------------------------------------------------------")
print("*********************************************************")
print("*********************************************************")
print("---------------------------------------------------------")
print("                      Test Set Analizi                   ")
print(test_df[["sales","year"]].describe().T)
print("---------------------------------------------------------")
for col in ['author', 'type', 'year']:
    print(f"\nSütun: {col}")
    print(test_df[col].value_counts())
    print("---------------------------------------------------------")
print("*********************************************************")