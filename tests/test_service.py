from app.data import all_deliveries, find_delivery


def test_service_contains_expected_number_of_deliveries():
    """The service should expose five delivery records."""
    assert len(all_deliveries()) == 5


def test_all_delivery_ids_are_unique():
    """Each delivery should have a unique ID."""
    deliveries = all_deliveries()

    ids = [delivery["id"] for delivery in deliveries]

    assert len(ids) == len(set(ids))


def test_nl1001_is_in_transit():
    """NL-1001 should be in transit."""
    delivery = find_delivery("NL-1001")

    assert delivery["status"] == "in_transit"


def test_nl1002_is_delivered():
    """NL-1002 should be delivered."""
    delivery = find_delivery("NL-1002")

    assert delivery["status"] == "delivered"


def test_nl1003_has_no_assigned_driver():
    """NL-1003 should not yet have a driver assigned."""
    delivery = find_delivery("NL-1003")

    assert delivery["driver"] is None


def test_delivery_record_contains_expected_fields():
    """Each delivery record should contain the required fields."""
    delivery = find_delivery("NL-1004")

    assert set(delivery.keys()) == {
        "id",
        "destination",
        "status",
        "driver",
    }