import os, subprocess, getpass

CONVERT_PARENT = '/tmp/Antiwiki/'

CONVERT_DIR=CONVERT_PARENT + str(os.getpid()) + '/'

WEB_ROOT = '/var/www/html/'

ODT = WEB_ROOT + 'odt/'

if not os.path.isdir(CONVERT_PARENT):
    os.mkdir(CONVERT_PARENT)

if not os.path.isdir(ODT):
    os.mkdir(ODT)

def add_navbar(doc):
	bar = """<div class="navbar">
	<a href="#download">Download</a>
	<a href="/cgi-bin/upload_page.py?doc={0}">Upload Revision</a>
</div>\n""".format(doc)

	with open(doc, 'r') as f:
		global cont
		cont = f.read()

	newdoc = doc + '.tmp'
	with open(doc + '.tmp', 'w') as f:
		f.write(bar + cont)

	os.remove(doc)
	os.rename(newdoc, doc)

def convert(odt, html_dir):
    os.mkdir(CONVERT_DIR)
    docname = os.path.basename(os.path.splitext(odt)[0])

    soffice_result = subprocess.run(['soffice', '--headless', '--convert-to', 'html:HTML', '--outdir', CONVERT_DIR, odt])
    if soffice_result.returncode != 0:
        os.remove(CONVERT_DIR) + docname + '.html'
        os.rmdir(CONVERT_DIR)
        raise Exception('Document conversion failed! Return code:' + str(soffice_result.returncode))
    add_navbar(CONVERT_DIR + docname + '.html')
    os.replace(CONVERT_DIR + docname + '.html', html_dir + docname + '.html')
    os.rmdir(CONVERT_DIR)

