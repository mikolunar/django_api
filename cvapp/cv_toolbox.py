import PyPDF2
# import json
# import io

# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfdevice import PDFDevice

# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams


# import pdfminer
# #from pdfminer.pdfinterp import process_pdf
# from pdfminer.converter import HTMLConverter, TextConverter

import contextlib
import tempfile
import textwrap


def load_PDF_text(filename):

    cv_json = {}
    pdf_file = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(pdf_file)

    pages = reader.pages

    cv_json['Pages'] = str(reader.getNumPages())

    for page in pages:
        # c.d. change this to load the PDF raw text into Django Database

        text = page.extractText()

    pdf_file.close()
    return text


# def parse_PDF_to_html(filename):

#     #     # Open a PDF file.
#     #     fp = open(filename, 'rb')
#     # # Create a PDF parser object associated with the file object.
#     #     parser = PDFParser(fp)
#     # # Create a PDF document object that stores the document structure.
#     # # Supply the password for initialization.
#     #     document = PDFDocument(parser)
#     # # Check if the document allows text extraction. If not, abort.
#     #     if not document.is_extractable:
#     #         raise PDFTextExtractionNotAllowed
#     #     # Create a PDF resource manager object that stores shared resources.
#     #     rsrcmgr = PDFResourceManager()
#     #     # Create a PDF device object.
#     #     device = PDFDevice(rsrcmgr)
#     #     # Create a PDF interpreter object.
#     #     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     #     # Process each page contained in the document.
#     #     for page in PDFPage.create_pages(document):
#     #         # (nterpreter.process_page(page))
#     #         print(page.contents())

#     rsrcmgr = PDFResourceManager()
#     retstr = io.StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = open(filename, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos = set()

#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
#         interpreter.process_page(page)

#     text = retstr.getvalue()

#     fp.close()
#     device.close()
#     retstr.close()
#     return text


# def pdf2html(in_file, out_file):
#     # https://github.com/scraperwiki/pdfminer/blob/scraperwiki/tools/pdf2html.cgi
#     rsrcmgr = PDFResourceManager()
#     laparams = LAParams()
#     converter = HTMLConverter
#     device = converter(rsrcmgr, out_file, codec='utf-8', laparams=laparams)
#     process_pdf(rsrcmgr, device, in_file, pagenos=[1,3,5], maxpages=9)

# # https://github.com/scraperwiki/scraperwiki-python/blob/master/scraperwiki/utils.py
#     with contextlib.closing(tempfile.NamedTemporaryFile(mode='r', suffix='.xml')) as xmlin:
#         cmd = 'pdftohtml -xml -nodrm -zoom 1.5 -enc UTF-8 -noframes "%s" "%s"' % (
#                 pdf_filename, xmlin.name.rpartition('.')[0])
#         os.system(cmd + " >/dev/null 2>&1")
#         result = xmlin.read().decode('utf-8')


def textformater(string):

    text = textwrap.fill(string, 10)

    return text


def numbers(number):

    max_len = len(str(int(number))+' ' + oct(number)
                  [2:]+' ' + hex(number)[2:].upper()+' '+bin(number)[2:])

    for i in range(1, number+1):
        row = str(int(i))+' ' + oct(i)[2:]+' ' + \
            hex(i)[2:].upper()+' '+bin(i)[2:]
        print(row.ljust(max_len, ' '))

    return ''


def numbers2(number):

    w = len("{0:b}".format(number))

    for i in range(1, number+1):
        # hex1=hex(i)[2:].upper()
        row = "{0:{w}d} {0:{w}o} {0:{w}X} {0:^{w}b}".format(i, w=w)
        print(row)

    return ''


def students():

    n = input()

    students = []
    for i in range(int(n)):
        name = str(input())
        grade = float(input())
        students.append([name, grade])

    # print(students)

    lowest_score = max(students, key=lambda item: item[1])[1]
    # print(lowest_score)

    lowest_list = list(filter(lambda x: x[1] == lowest_score, students))

    # print(lowest_list)

    for student in students:
        if student[1] == lowest_score:
            students.remove(student)

    # print(students)

    second_lowest_score = max(students, key=lambda item: item[1])[1]
    # print(second_lowest_score)

    second_lowest_list = list(filter(
        lambda x: x[1] == second_lowest_score, students))

    # print(second_lowest_list)

    final = second_lowest_list
   # print(final)
    final.sort(key=lambda item: item[0])

    print(final)
    for student in final:
        print(student[0])


def exceptions():

    try:
        f = open('../cv1.pdf')
    except Exception as e:
        print("!!!!!! not found" + str(e))


if __name__ == "__main__":
    exceptions()
