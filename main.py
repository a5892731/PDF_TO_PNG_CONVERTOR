'''
author: a5892731
creation date: 2021-11-01
last update:...
version: 1.0
'''


from pdf2image import convert_from_path

class File:
    def __init__(self, file_path):
        self.size_x = 0
        self.size_y = 0
        self.dpi_size = 500
        self.file_path = file_path
        self.pages = None
        self.poppler_path = r"C:\Users\a5892\poppler-21.10.0\Library\bin"   # red about this path in READ_ME file!

class PdfFile(File):
    def import_pdf_file_pages(self):
        self.pages = convert_from_path(pdf_path=self.file_path, dpi= self.dpi_size,
                                       poppler_path=self.poppler_path,
                                       )

    def convert_pdf_to_png(self, filename):
        for page in self.pages:
            page.save('png/{}.png'.format(filename), 'PNG')


#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    filename = "file1"

    pdf_object = PdfFile('pdf/{}.pdf'.format(filename))
    pdf_object.import_pdf_file_pages()
    pdf_object.convert_pdf_to_png(filename)