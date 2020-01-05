#!/usr/bin/env python3

import cgi, cgitb, os

cgitb.enable()

qstring = os.environ['QUERY_STRING']
category = qstring.split('=')[1]

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
	<p>Upload Revision of {0}.
	<form enctype="multipart/form-data" action="/cgi-bin/new_category.py?category={0}" method="post">
		<p>Category Name: <input type="text" id="category"/>
		<p><input type="submit" value="create"/>
	</form>
</body>
</html>""".format(category)

print(output)
