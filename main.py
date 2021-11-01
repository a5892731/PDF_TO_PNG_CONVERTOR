'''
author: a5892731
creation date: 2021-11-01
last update:2021-11-01
version: 1.1
    -add file browser function
'''


from pdf2image import convert_from_path
import os

class File:
    def __init__(self, filename, input_path, output_path, input_file_type):
        self.size_x = 0
        self.size_y = 0
        self.dpi_size = 500
        self.file_path = input_path + "/" + filename + input_file_type
        self.pages = None
        self.poppler_path = r"C:\Users\a5892\poppler-21.10.0\Library\bin"   # red about this path in READ_ME file!


class PdfFile(File):
    def __init__(self, filename, input_path = "pdf", output_path = 'png', input_file_type = ".pdf"):
        super().__init__(filename, input_path, output_path, input_file_type)

        self.import_pdf_file_pages()

        if output_path == "png":
            self.convert_pdf_to_png(filename)
        else:
            print("wrong format")


    def import_pdf_file_pages(self):
        self.pages = convert_from_path(pdf_path=self.file_path, dpi= self.dpi_size,
                                       poppler_path=self.poppler_path, timeout=600
                                       )

    def convert_pdf_to_png(self, filename, output_path = 'png'):
        for page in self.pages:
            page.save('{}/{}.png'.format(output_path, filename), 'PNG')
#----------------------------------------------------------------------------------------------------------------------
class FileBrowser:
    def __init__(self, input_path = "pdf", output_path = "png", input_file_type = ".pdf"):
        self.input_path = input_path
        self.output_path = output_path
        self.input_file_type = input_file_type

    def file_path_extracter(self, FileObject):
        for root, dirs, files in os.walk(self.input_path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
                path_len = len(self.input_path) + 1  #extra 1 for / sign
                file_name = os.path.join(root, name).rstrip(".pdf")[path_len::]
                print(file_name)

                FileObject(file_name, self.input_path, self.output_path, self.input_file_type)

        print("process finished")

#----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    filename = "file1"


    generator = FileBrowser()
    generator.file_path_extracter(PdfFile)

