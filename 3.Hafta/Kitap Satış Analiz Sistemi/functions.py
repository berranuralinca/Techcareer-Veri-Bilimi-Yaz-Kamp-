# 1. Fonksiyon Yazma:
# most_popular_boo(books) → En çok satan kitabın bilgilerini döndürsün.
# sales_author(books) → Her yazarın toplam satışını bir sözlük olarak döndürsün.

def most_popular_book(books):
    #En çok satan kitabın bilgilerini döndürsün.
    max_value = max(books, key=lambda k: k['sales'])
    return max_value["name"]


def sales_author(books):
    # Her yazarın toplam satışını bir sözlük olarak döndürsün.
    sales_list = {}  
    for book in books:
        author = book['author']
        sales = book['sales']
        if author in sales_list:
            sales_list[author] += sales
        else:
            sales_list[author] = sales
    return sales_list