import requests

from asucourseparser import ASUCoursesHTMLParser


# TODO: wrap in class
def get_response(url):
    return requests.get(url)


def poll_site(url):
    response = get_response(url)
    # TODO: modularize parsers
    parser = ASUCoursesHTMLParser()
    parser.feed(response.text)
    return parser.courses
