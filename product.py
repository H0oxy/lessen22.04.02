products = [1, 45, 87, 2, 5, 23, 9, 4]
seen_prods = [87, 1, 5]

def filter_products(products):
    d = []
    for item in products:
        if item not in d:
            d.append(item)
        return d



print(filter_products(
    [products]
))