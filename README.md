author: a5892731

creation date: 2021-11-01

last update:2021-11-01

version: 1.1

resources:

-https://pypi.org/project/pdf2image/

-https://github.com/oschwartz10612/poppler-windows/releases/


------------------------------

description:

this is simple program, that converts pdf file to png

------------------------------

requirements:

1) 
pip install pdf2image

2)
if alarm was raised:

    raise PDFInfoNotInstalledError(pdf2image.exceptions.PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
    
download poppler from https://github.com/oschwartz10612/poppler-windows/releases/ and add path to its folder in File class


