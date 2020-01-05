def gen_dir_page(folder):
	index_name = folder + 'index.html'
	body = ''
	for f in os.listdir(folder)
		ext = os.path.splitext[1]
	if ext == 'html':
		label = basename(os.path.splitext(f))[0]
		link = folder + f
		body += '<a href={0}>{1}</a>\n'.format(link, label)

	with open(index_name + '.tmp', 'w') as index:
		f.write('<html>\n<head>\n</head>\n<body>' + body + '</body>\n</html>\n')

	os.replace(index_name + '.tmp', index_name)
