import pytest
from unittest.mock import patch
from modules.URL_shortener import url_shorten

@patch('requests.get')
def test_url_shorten(mock_get):
    mock_get.return_value.json.return_value = {
        "data": {
            "url": "https://ulvis.net/shortened_url"
        }
    }
    input_url = "https://example.com"
    shortened_url = url_shorten(input_url)
    assert shortened_url == "https://ulvis.net/shortened_url"

@patch('requests.get')
def test_url_shorten_invalid(mock_get):
    mock_get.return_value.json.return_value = {}
    input_url = "https://example.com"
    assert url_shorten(input_url) == "Wrong type of input. Please enter a valid URL."
