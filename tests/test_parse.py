"""
Unit tests for mock-server simple_parse function.
Tests use only synthetic inputs from examples/synthetic/.
"""
import sys
import os

# Add mock-server to path so we can import app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../mock-server"))

from app import simple_parse


def test_parse_date_normalization():
    """Test that dates are normalized to YYYY-MM-DD format."""
    text = "04/06/2024: applied compost 100kg/ha"
    result = simple_parse(text)
    assert result["date"] == "2024-06-04", f"Expected 2024-06-04, got {result['date']}"


def test_parse_crop_detection():
    """Test that crop types are correctly identified."""
    text = "sowed millet"
    result = simple_parse(text)
    assert result["crop"] == "millet", f"Expected millet, got {result['crop']}"


def test_parse_practice_type_fertilizer():
    """Test that fertilizer practice is detected."""
    text = "applied compost 100kg/ha"
    result = simple_parse(text)
    assert result["practice_type"] == "fertilizer", f"Expected fertilizer, got {result['practice_type']}"


def test_parse_practice_type_planting():
    """Test that planting practice is detected."""
    text = "sowed wheat"
    result = simple_parse(text)
    assert result["practice_type"] == "planting", f"Expected planting, got {result['practice_type']}"


def test_parse_amount_detection():
    """Test that amounts are extracted."""
    text = "applied 50 kg/ha urea"
    result = simple_parse(text)
    assert result["amount"] is not None, "Expected amount to be detected"
    assert "50" in result["amount"], f"Expected 50 in amount, got {result['amount']}"


def test_parse_product_detection():
    """Test that product names are extracted."""
    text = "applied dap fertilizer"
    result = simple_parse(text)
    assert result["product"] == "dap", f"Expected dap, got {result['product']}"


def test_parse_empty_input():
    """Test handling of empty input."""
    text = ""
    result = simple_parse(text)
    assert result is not None, "Should return a dict even for empty input"
    assert result["notes"] == "", "Notes should be empty string for empty input"


def test_parse_complex_text():
    """Test parsing a realistic farmer practice log entry."""
    text = "15/11/2023: irrigated and applied urea 50 kg/ha for rice"
    result = simple_parse(text)
    assert result["date"] == "2023-11-15", f"Expected 2023-11-15, got {result['date']}"
    assert result["crop"] == "rice", f"Expected rice, got {result['crop']}"
    assert "50" in result["amount"], f"Expected 50 in amount, got {result['amount']}"


if __name__ == "__main__":
    # Simple test runner (use pytest for full test suite)
    test_parse_date_normalization()
    test_parse_crop_detection()
    test_parse_practice_type_fertilizer()
    test_parse_practice_type_planting()
    test_parse_amount_detection()
    test_parse_product_detection()
    test_parse_empty_input()
    test_parse_complex_text()
    print("✓ All tests passed!")
