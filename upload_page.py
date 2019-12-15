#!/usr/bin/env python3

import cgi, cgitb, os

cgitb.enable()

qstring = os.environ['QUERY_STRING']

doc = qstring.split('=')[1]

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
	<p>Upload Revision of {0}.
	<form enctype="multipart/form-data" action="/cgi-bin/upload.py" method="post">
		<p>Select File: <input type="file" name="filename"/>
		<p><input type="submit" value="upload"/>
	</form>
</body>
</html>""".format(doc)

print(output)

