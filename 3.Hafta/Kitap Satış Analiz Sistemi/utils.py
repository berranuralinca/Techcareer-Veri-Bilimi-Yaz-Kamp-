# 2. Liste ve Küme İşlemleri:
# Tüm kitap türlerini (tur) küme halinde çıkarın (tekrar eden türler olmadan).
def book_types(books):
    types = set(book["type"] for book in books)
    return types

# Satış adedi 1000’den fazla olan kitapların isimlerini bir listede toplayın.
def most_popular(books):
    sales_list = list(map(lambda k: k["name"], filter(lambda x: x["sales"] > 1000, books)))
    return sales_list


# 3. Lambda / Filter / Map Kullanımı:
# filter ile 2020’den sonra çıkan ı süzün.
def filter_year(books,year=2020):
    filtered_list = list(map(lambda k: k["name"], filter(lambda x: x["year"] > 2020, books)))
    return filtered_list

# map ile tüm satış adetlerini %10 artırılmış şekilde yeni bir listeye aktarın.
def sales_count(books):
    ten_percent = list(map(lambda k: (k["name"], k["sales"] * 1.1),books ))
    return ten_percent

# sorted + lambda ile ı satış miktarına göre azalan şekilde sıralayın.
def sorted_sales(books):
    sorted_list = sorted(books, key=lambda k: k["sales"], reverse=True)
    return sorted_list