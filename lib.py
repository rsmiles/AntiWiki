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

def gen_dir_page(folder):
	index_name = folder + 'index.html'
	body = ''
	for f in os.listdir(folder)
		ext = os.path.splitext[1]
	if ext == 'html':
		label = basename(os.path.splitext(f))[0]
		link = folder + f
		body += '<a href={0}>{1}</a>\n'.format(link, label)

	navbar = """<div class="navbar">
<a href="/pages">Top</a>
</div>
"""

	with open(index_name + '.tmp', 'w') as index:
		f.write('<html>\n<head>' + navbar + '</head>\n<body>' + body + '</body>\n</html>\n')

	os.replace(index_name + '.tmp', index_name)

