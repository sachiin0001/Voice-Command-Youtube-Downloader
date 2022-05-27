from googlesearch import search,get
from bs4 import BeautifulSoup


def findurls(term,result = 10):
    urls = search(term)
    response = get(urls[4]).text
    soup = BeautifulSoup(response,"html.parser")
    soup.prettify()
    summary = ""
    for div in soup.find_all("div"):
        if div.string:
            summary += (str(div.string) + "\n")
    #https://pypi.org/project/pysummarization/
    print(summary)

