#!/usr/bin/env python3

import cgi, cgitb, os, subprocess
from config import *

def add_navbar(doc, truepath):
	odtpath = os.path.splitext(truepath)[0] + '.odt'

	bar = """<div class="navbar">
	<a href="/pages">Explore</a>
	<a href="/odt/{0}">Download</a>
	<a href="/cgi-bin/upload_page.py?doc={1}">Upload Revision</a>
</div>\n""".format(odtpath, truepath)

	with open(doc, 'r') as f:
		global cont
		cont = f.read()

	newdoc = doc + '.tmp'
	with open(doc + '.tmp', 'w') as f:
		f.write(bar + cont)

	os.replace(newdoc, doc)

def convert(odt, html_dir):
	os.mkdir(CONVERT_DIR)
	docname = os.path.basename(os.path.splitext(odt)[0])

	soffice_result = subprocess.run(['soffice', '--headless', '--convert-to', 'html:HTML', '--outdir', CONVERT_DIR, ODT + odt])
	if soffice_result.returncode != 0:
		os.remove(CONVERT_DIR) + docname + '.html'
		os.rmdir(CONVERT_DIR)
		raise Exception('Document conversion failed! Return code:' + str(soffice_result.returncode))
	add_navbar(CONVERT_DIR + docname + '.html', html_dir + docname + '.html')
	os.replace(CONVERT_DIR + docname + '.html', WEB_ROOT + html_dir + docname + '.html')
	os.rmdir(CONVERT_DIR)


cgitb.enable()
form = cgi.FieldStorage()

qstring = os.environ['QUERY_STRING']
doc = os.path.splitext(qstring.split('=')[1])[0]

result = ''

fileitem=form['filename']
if fileitem.filename:
	filename = os.path.basename(fileitem.filename.replace('\\', '/'))
	with open(ODT + doc + '.odt', 'wb') as f:
		f.write(fileitem.file.read())
	result = """<p>FILE "{0}" uploaded.</p>
	<a href="/{1}.html">click here to return to {1}</a>""".format(filename, doc, ODT + doc + '.odt', WEB_ROOT + doc + '.html')
	convert(doc + '.odt', os.path.dirname(doc))
else:
	result = '<p>No file was provided<\p>'

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
	{0}
</body>
</html>\
""".format(result)

print(output)

