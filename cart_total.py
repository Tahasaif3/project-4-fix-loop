def total_price(unit_price, quantity):
    if quantity > 10:
        discount = 0.15
    elif quantity > 5:
        discount = 0.05
    else:
        discount = 0.0
    subtotal = unit_price * quantity
    return round(subtotal - (subtotal * discount), 2)
