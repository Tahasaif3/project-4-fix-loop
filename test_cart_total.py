from cart_total import total_price


def test_no_discount_under_five():
    assert total_price(10, 3) == 30.0


def test_five_percent_at_exactly_five():
    assert total_price(10, 5) == 47.5


def test_fifteen_percent_at_exactly_ten():
    assert total_price(10, 10) == 85.0
