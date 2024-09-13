import re

def extract_date(url):
    regex = re.compile(r'(\d{4})/(\d{1,2})/(\d){1,2}')
    mo = regex.findall(url)
    return mo

url = 'https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/'

extract_date(url)