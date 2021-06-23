import requests

from myparser import MyHTMLParser


def get_response(url):
    return requests.get(url)


def poll_site(url):
    response = get_response(url)
    parser = MyHTMLParser()
    parser.feed(response.text)
    print(parser.courses)
    return response
