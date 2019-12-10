import os
import subprocess

CONVERT_DIR='./tmp'

def add_navbar():
    navbar = """\
\   <div class="navbar">
\	<a href="#download">Download</a>
\	<a href="#upload_revision">Upload Revision</a>
\    </div>"""

def convert_doc(odt, html):
    fname = os.path.basename(odt)
    outdir = os.path.dirname(html)
    outname = os.path.basename(os.path.splitext(html)[0])
    subprocess.run(['cp', 'odt', CONVERT_DIR + fname])
    subprocess.run(['soffice', '--headless', '--convert', 'html', CONVERT_DIR + fname])
    for f in os.listdir(CONVERT_DIR):
        if f != fname:
            ext = os.path.splitext(f)[1]
            os.rename(CONVERT_DIR + '/' + f, outdir + '/' + outname + ext)
        os.remove(CONVERT_DIR + '/' + fname)


