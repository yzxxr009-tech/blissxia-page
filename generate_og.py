import weasyprint
import sys
from PIL import Image
import fitz

html_path = sys.argv[1]
png_path = sys.argv[2]

doc = weasyprint.HTML(filename=html_path)
pdf_bytes = doc.write_pdf()
doc_pdf = fitz.open("pdf", pdf_bytes)
page = doc_pdf.load_page(0)
pix = page.get_pixmap(dpi=96)
pix.save(png_path)
doc_pdf.close()

img = Image.open(png_path)
print(f"Generated: {png_path} ({img.size[0]}x{img.size[1]})")
