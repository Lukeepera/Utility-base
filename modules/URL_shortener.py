import requests

def url_shorten(inputed_url):
    try:
        url = f"https://ulvis.net/API/write/get?url={inputed_url}"
        result = requests.get(url)
        jsoned_info = result.json()
        shortened_url = jsoned_info["data"]["url"]

        return shortened_url

    except Exception:
        return "Wrong type of input or Proxy-error (API not enabled) !"
