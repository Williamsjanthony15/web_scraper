from bs4 import BeautifulSoup
from bs4.builder import ParserRejectedMarkup
import requests

wiki = https://en.wikipedia.org/wiki/History_of_Mexico
requestsVar = requests.get(wiki)
information = BeautifulSoup(requestsVar.content, 'html.parser')

info_results = information.find(class_ = 'reference')

references = info_results.find_all('cit_ref- ')

cites = info_results('')
""" Count Function Must be named (get_citations_needed_count)"""
""" takes in a URL and Returns an Integer"""


def get_citations_needed_count():
    print('getting citations for count')




""" Report Function must be named (get_citations_needed_report)"""
""" Takes in a URL and Returns a String"""
""" the string should be formatted with each citation needed on ownline, in order found"""


def get_citations_needed_report():
    print('getting citations for report')
