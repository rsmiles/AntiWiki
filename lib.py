import os, subprocess

CONVERT_PARENT = '/tmp/Antiwiki/'

CONVERT_DIR=CONVERT_PARENT + str(os.getpid()) + '/'

if not os.path.isdir(CONVERT_PARENT):
    os.mkdir(CONVERT_PARENT)

def add_navbar(doc):
	bar = """
<div class="navbar">
	<a href="#download">Download</a>
	<a href="/cgi-bin/upload.py?doc={0}">Upload Revision</a>
</div>\n""".format(doc)

	with open(doc, 'r') as f:
		global cont
		cont = f.read()

	newdoc = doc + '.tmp'
	with open(doc + '.tmp', 'w') as f:
		f.write(bar + cont)

	os.remove(doc)
	os.rename(newdoc, doc)

def convert(odt, html):
    os.mkdir(CONVERT_DIR)
    fname = os.path.basename(odt)
    outdir = os.path.dirname(html) + '/'
    if outdir == '/': # make sure we don't accidentally try to place output in root
        outdir = ''
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

