import os, subprocess

CONVERT_PARENT = '/tmp/AntiWiki/'

CONVERT_DIR=CONVERT_PARENT + str(os.getpid()) + '/'

if not os.path.isdir(CONVERT_PARENT):
    os.mkdir(CONVERT_PARENT)

def navbar(doc):
    bar = """\
\   <div class="navbar">
\	\	<a href="#download">Download</a>
\	\	<a href="#upload_revision">Upload Revision</a>
\    </div>\n"""
	with open(doc, 'r') as f:
		global cont
		cont = f.read()

	newdoc = doc + '.tmp'
	with open(doc + '.tmp') as f:
		cont.write(bar + doc)

	os.remove(doc)
	os.rename(newdoc, doc)

def convert(odt, html):
    os.mkdir(CONVERT_DIR)
    fname = os.path.basename(odt)
    outdir = os.path.dirname(html) + '/'
    outname = os.path.basename(os.path.splitext(html)[0])
    subprocess.run(['cp', odt, CONVERT_DIR + fname])
    olddir=os.getcwd()
    os.chdir(CONVERT_DIR)
    subprocess.run(['soffice', '--headless', '--convert-to', 'html', fname])
    os.chdir(olddir)
    for f in os.listdir(CONVERT_DIR):
        if f != fname:
            ext = os.path.splitext(f)[1]
            os.rename(CONVERT_DIR + f, outdir + outname + ext)
    for f in os.listdir(CONVERT_DIR):
        os.remove(CONVERT_DIR + '/' + f)
    os.rmdir(CONVERT_DIR)

