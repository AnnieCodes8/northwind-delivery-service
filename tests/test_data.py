from app.data import all_deliveries, find_delivery


def test_find_known_delivery():
    delivery = find_delivery("NL-1002")

    assert delivery is not None
    assert delivery["destination"] == "Bristol"
    assert delivery["status"] == "delivered"


def test_unknown_delivery_returns_none():
    assert find_delivery("NL-9999") is None


def test_delivery_data_is_copied():
    delivery = find_delivery("NL-1001")

    delivery["destination"] = "London"

    original = find_delivery("NL-1001")

    assert original["destination"] == "Manchester"