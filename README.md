author: a5892731
creation date: 2021-11-01
last update:...
version: 1.0

resources:
-https://pypi.org/project/pdf2image/
-https://github.com/oschwartz10612/poppler-windows/releases/


requirements
if:
    raise PDFInfoNotInstalledError(
    pdf2image.exceptions.PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
download poppler from https://github.com/oschwartz10612/poppler-windows/releases/ and add path to its folder in File class