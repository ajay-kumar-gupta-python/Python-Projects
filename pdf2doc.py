from pdf2docx import Converter
old_pdf="file_name.pdf"
new_doc="new_file name"

obj=Converter(old_pdf)
obj.convert(new_doc)
obj.close()




