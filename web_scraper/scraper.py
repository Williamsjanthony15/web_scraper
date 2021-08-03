from bs4 import BeautifulSoup
from bs4.builder import ParserRejectedMarkup
import requests

 
""" Count Function Must be named (get_citations_needed_count)"""
""" takes in a URL and Returns an Integer"""


def get_citations_needed_count(wiki):
    requestsVar = requests.get(wiki)
    information = BeautifulSoup(requestsVar.content, 'html.parser')
    references = information.find_all('a')
    count = 0
    
    for reference in references:
        text = reference.get_text()
        if "citation needed" in text:
            count += 1
    return count



""" Report Function must be named (get_citations_needed_report)"""
""" Takes in a URL and Returns a String"""
""" the string should be formatted with each citation needed on ownline, in order found"""


def get_citations_needed_report(wiki):
    requestsVar = requests.get(wiki)
    information = BeautifulSoup(requestsVar.content, 'html.parser')
    references = information.find_all('a')
    report = ''
    for reference in references:
        text = reference.get_text()
        if 'citation needed' in text:
            report += '***** Citation Needed *****\n'
            report += reference.parent.parent.parent.get_text() + '\n'
    return report 


def get_citation_headings(wiki):
    headings = []
    page = requests.get(wiki)
    soup = BeautifulSoup(page.content, "html.parser")
    references = soup.find_all('a')
    headings_tags  = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for reference in references:
        text = references.get_text()
        if 'Citation Needed' in text:
            elem = reference.parent.parent.parent
            for ps in elem.previous_siblings:
                if ps.name in headings_tags:
                    headings.append(ps.text)
                    break
    return headings


if __name__ == '__main__':
    wiki = https://en.wikipedia.org/wiki/History_of_Mexico
    count = get_citations_needed_count

    report = get_citations_needed_report

    headings = get_citation_headings

