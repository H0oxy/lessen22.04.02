products = [1, 45, 87, 2, 5, 23, 9, 4]
seen_prods = [87, 1, 5]
d = []
def filter_products(products, seen_prods):
    for item in products, seen_prods:
        if item not in d:
            d.append(item)



print(filter_products(
        [products],
        [seen_prods],
))