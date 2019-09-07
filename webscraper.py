from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'https://prairielearn.engr.illinois.edu/pl/course_instance/32724/assessments'
    response = simple_get(url)

    #print (is_good_response(response))
    #print (response)

    print ("helloWorld")
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        homework_names = set()
        for div in html.select('div'):
            print (div)
            for td in html.select('td'):
                print (td['class'])
                if td['class'] == "badge color-green1 color-hover":
                    homework_names.append(td.text)
        return homework_names

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

print(get_names())


