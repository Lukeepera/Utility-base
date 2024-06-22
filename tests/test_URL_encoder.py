from modules.URL_encoder import url_encode, url_decode

def test_url_encode():
    input_string = "hello world"
    expected_output = "hello+world"
    assert url_encode(input_string) == expected_output

    input_string = "hello world!"
    expected_output = "hello+world%21"
    assert url_encode(input_string) == expected_output

def test_url_decode():
    encoded_string = "hello+world"
    expected_output = "hello world"
    assert url_decode(encoded_string) == expected_output

    encoded_string = "hello+world%21"
    expected_output = "hello world!"
    assert url_decode(encoded_string) == expected_output
