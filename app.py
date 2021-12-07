
PDFTOPPMPATH = r"C:\Program Files (x86)\poppler-0.68.0\bin\pdftoppm.exe"
PDFFILE = "teste.pdf"

import subprocess
subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))