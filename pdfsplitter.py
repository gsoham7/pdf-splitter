from PyPDF2 import PdfWriter, PdfReader

def cropper(start, end, file):
    input_pdf = PdfReader(open(file, "rb"))
    out_pdf = PdfWriter()

    cropped_filename = file.split(".")[0] + "_cropped.pdf"

    with open(cropped_filename, "wb") as ostream:
        for page_num in range(start - 1, end):  # Adjust page indexing
            out_pdf.add_page(input_pdf.pages[page_num])
        out_pdf.write(ostream)

    return cropped_filename





