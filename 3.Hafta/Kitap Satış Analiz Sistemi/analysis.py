import statistics 

# 4. İstatistiksel Analiz:
# Ortalama satış adedini bulun.
def average_sales(books):
    average = statistics.mean([book["sales"] for book in books])
    return average

# En çok satış yapan türü bulun.
def popular_type(books):
    sales_type = {}

    for book in books:
        type_book = book["type"]
        sales = book["sales"]
        if type_book in sales_type:
            sales_type[type_book] += sales
        else:
            sales_type[type_book] = sales

    max_sales = [t for t, s in sales_type.items() if s == max(sales_type.values())]
    return max_sales

# Satışların standart sapmasını hesaplamak için statistics modülünü kullanın.
def std_dev(books):
    return statistics.stdev([k['sales'] for k in books])