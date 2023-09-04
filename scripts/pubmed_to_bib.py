import argparse
import os
import urllib.error
from Bio import Entrez
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

def get_pubmed_info(pubmed_id):
    Entrez.email = 'your.email@example.com'
    try:
        handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    except urllib.error.HTTPError as err:
        print(f"HTTP Error occurred while fetching Pubmed ID {pubmed_id}: {err}")
        return None

    record = Entrez.read(handle)
    if 'PubmedArticle' not in record or not record['PubmedArticle']:
        return None

    article = record['PubmedArticle'][0]['MedlineCitation']['Article']
    authors = [i['ForeName'] + ' ' + i['LastName'] for i in article['AuthorList']]

    # Fetch DOI using Entrez.efetch
    doi = None
    for id_info in record['PubmedArticle'][0]['PubmedData']['ArticleIdList']:
        if id_info.attributes['IdType'] == 'doi':
            doi = id_info.title()
            break

    article_info = {
        'title': article['ArticleTitle'],
        'journal': article['Journal']['Title'],
        'year': article['Journal']['JournalIssue']['PubDate']['Year'],
        'doi': doi if doi else "DOI not found",
        'author': ' and '.join(authors),
        'abstract': article['Abstract']['AbstractText'][0] if 'Abstract' in article and 'AbstractText' in article['Abstract'] else "",
        'first_author_lastname': authors[0].split(' ')[-1] if authors else ""
    }
    return article_info

def write_bibtex_file(article_info, file_name, pdf_link=None):
    db = BibDatabase()
    entry = {
        'journal': article_info['journal'],
        'title': article_info['title'],
        'year': article_info['year'],
        'doi': article_info['doi'],
        'author': article_info['author'],
        'abstract': article_info['abstract'],
        'ENTRYTYPE': 'article',
        'ID': file_name
    }
    if pdf_link:
        entry['pdf'] = pdf_link
    ordered_fields = ['ENTRYTYPE', 'ID', 'journal', 'title', 'year', 'doi', 'author', 'pdf', 'abstract']
    entry = {field: entry[field] for field in ordered_fields if field in entry}
    db.entries = [entry]
    writer = BibTexWriter()
    with open(file_name + '.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download Bibtex file for given Pubmed ID')
    parser.add_argument('pubmed_id', help='Pubmed ID to fetch Bibtex for')
    parser.add_argument('-n', '--name', help='Optional custom name for the bibtex file')
    parser.add_argument('--with_pdf', help='Optional PDF link to be included in the bibtex file')
    args = parser.parse_args()

    article_info = get_pubmed_info(args.pubmed_id)
    if article_info is None:
        print(f"No article found or error occurred while fetching Pubmed ID: {args.pubmed_id}")
    else:
        if args.name:
            file_name = args.name
        else:
            file_name = article_info['first_author_lastname'] + '_' + args.pubmed_id
        write_bibtex_file(article_info, file_name, pdf_link=args.with_pdf)
