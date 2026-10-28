import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status

def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0

def test_carry_on_ok():
    assert carry_on_ok(5, 1, False) is True

def test_baggage_fee_errors():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -5, "domestic", False)

def test_baggage_fee_cabins_and_members():
    assert baggage_fee("premium", 40, "domestic", True) == 100
    assert baggage_fee("business", 45, "international", True) == 225

def test_baggage_fee_excess_thresholds():
    assert baggage_fee("economy", 40, "international", False) == 2500
    assert baggage_fee("economy", 40, "domestic", False) == 25 * 40

def test_carry_on_edge_cases():
    assert carry_on_ok(5, 2, True) is True
    assert carry_on_ok(5, 3, True) is False
    assert carry_on_ok(8, 1, False) is False

def test_check_in_status_paths():
    assert check_in_status(130, True, True) == "open"
    assert check_in_status(110, True, True) == "late"
    assert check_in_status(90, True, True) == "closed"
    assert check_in_status(40, False, False) == "late"
    assert check_in_status(20, False, False) == "closed"
