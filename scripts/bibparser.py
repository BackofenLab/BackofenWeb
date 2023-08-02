import argparse
import bibtexparser
import re

from jinja2 import Template

# Dictionary to replace author names with aliases for the data column (does not affect the displayed author names)
ALIAS_DICT = {"S. Lange"              : "Sita J. Saunders",
              "S. J. Lange"           : "Sita J. Saunders",
              "S. J. Saunders"        : "Sita J. Saunders",
              "Sita J. Lange"         : "Sita J. Saunders",
              "R. Backofen"           : "Rolf Backofen",
              "Martin Mann"           : "Martin Raden",
              "M. Mann"               : "Martin Raden",
              "Bjorn Gruning"         : "Björn Grüning",
              "Bjorn Grüning"         : "Björn Grüning",
              "Björn Gruning"         : "Björn Grüning",
              "Bjoern Gruening"       : "Björn Grüning",
              "Björn A. Grüning"      : "Björn Grüning",
              "Björn A Grüning"       : "Björn Grüning",
              "Björn Andreas Grüning" : "Björn Grüning",
              "Berenice Batut"        : "Bérénice Batut",
              "Tran Van Dinh"         : "Van Dinh Tran",
              "Dinh Van Tran"         : "Van Dinh Tran",
              "Dinh V Tran"           : "Van Dinh Tran",
              "Omer Alkhnbashi"       : "Omer S. Alkhnbashi",
              "Omer S Alkhnbashi"     : "Omer S. Alkhnbashi"}

TYPE_DICT = {"article"              : "Article",
             "inproceedings"        : "Conference",
             "proceedings"          : "Conference",
             "conference"           : "Conference",
             "incollection"         : "Book",
             "inbook"               : "Book",
             "book"                 : "Book",
             "booklet"              : "Book",
             "PhDThesis"            : "PhD Thesis",
             "mastersthesis"        : "Master's Thesis",
             "default"              : "Other"}

template_string = '''
<div class="publication" data-author="{{ authors_data }}" data-journal="{{ journal }}" data-year="{{ year }}" data-type="{{ type }}">
    <div class="title" name="{{ id }}">
        <a href="{{ href }}">{{ title }}</a>
    </div>
    <div class="authors">
        {{ authors }}
    </div>
    <div class="journal">
        {{ journal }}, {{ year }}
    </div>
    <div class="button-container">
        {%- if link %}
        <div class="link">
            <a href="{{ href }}">DOI</a>
        </div>
        {%- endif %}
        <div class="bibtex-file">
            <a href="{{ bibtex_file_href }}">BIB</a>
        </div>
        {%- if pdf_href %}
        <div class="pdf-file">
            <a href="{{ pdf_href }}">PDF</a>
        </div>
        {%- endif %}
    </div>
</div>
'''

template = Template(template_string)

def format_authors(authors):
    # Replace newlines with space and collapse multiple spaces into one
    authors = authors.replace("\n", " ")
    authors = re.sub(r'\s+', ' ', authors)

    author_list = authors.split(' and ')
    authors_list = []
    for author in author_list:
        parts = [part.strip() for part in author.split(',')]
        last_name = parts[0]
        first_name = " ".join(parts[1:])  # first name includes all parts except the last
        full_name = f'{first_name} {last_name}'

        full_name = full_name.strip()
        # Check if the author name is in the alias dictionary
        if full_name in ALIAS_DICT:
            full_name = ALIAS_DICT[full_name]

        authors_list.append(full_name)

    authors_data = ";".join(authors_list)

    if len(authors_list) > 1:
        last_author = authors_list.pop()
        authors_formatted = ', '.join(authors_list) + ' and ' + last_author
    else:
        authors_formatted = authors_list[0]

    return authors_formatted, authors_data

def format_title(title):
    return re.sub(r'\{(.+?)\}', r'\1', title)

def create_html_page(bib_entries, output_file):
    html_string = ''

    # Sort entries by year (descending) and first author's name
    bib_entries.sort(key=lambda e: (-int(e.get('year', '0')), e.get('author', '').split(' and ')[0].split(',')[0]))

    for entry in bib_entries:
        id = entry.get('ID', '')
        authors, authors_data = format_authors(entry.get('author', ''))
        journal = entry.get('journal', '')
        journal = journal if journal else format_title(entry.get('booktitle', '').replace("\n", " "))
        year = entry.get('year', '')
        title = format_title(entry.get('title', '').replace("\n", " "))
        link = entry.get('doi', entry.get('url', ''))
        href = f"https://doi.org/{link}" if not link.startswith(('http', 'www')) else link
        entry_type = entry.get('ENTRYTYPE', '')  # New line to get entry type
        if entry_type in TYPE_DICT:
            entry_type = TYPE_DICT[entry_type]
        else:
            entry_type = TYPE_DICT["default"]

        bibtex_file_href = f"https://github.com/RickGelhausen/webtests/blob/main/bibtex/{id}.bib"

        pdf_href = entry.get('pdf', '')

        html_string += template.render(id=id, authors_data=authors_data, authors=authors, journal=journal, year=year, title=title, link=link, href=href, type=entry_type, bibtex_file_href=bibtex_file_href, pdf_href=pdf_href)  # Updated to pass entry type to template

    with open(output_file, 'w') as f:
        f.write(html_string)

def main():
    parser = argparse.ArgumentParser(description='Convert a .bib file into an HTML page')
    parser.add_argument('-i', '--input', help='The .bib file to parse', required=True)
    parser.add_argument('-o', '--output', help='The output HTML file name', required=True)

    args = parser.parse_args()

    with open(args.input) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    create_html_page(bib_database.entries, args.output)

if __name__ == '__main__':
    main()