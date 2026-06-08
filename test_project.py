from project import extract_rate, clean_currency, validate_currency

def test_extract_rate():
    fake_dict = {
        "THB": 32.62,
        "JPY": 159.87,
        "EUR": 0.85
    }
    assert extract_rate("JPY", fake_dict) == 159.87
    assert extract_rate("EUR", fake_dict) == 0.85

def test_clean_currency():
    assert clean_currency("jpy") == "JPY"
    assert clean_currency("  thb  ") == "THB"
    assert clean_currency("Usd") == "USD"

def test_validate_currency():
    fake_dict = {
        "THB": 32.62,
        "JPY": 159.87
    }
    assert validate_currency("JPY", fake_dict) is True
    assert validate_currency("ABC", fake_dict) is False
