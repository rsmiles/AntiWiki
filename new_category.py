#!/usr/bin/env python3

import cgi, cgitb, os
from config import *
from lib import *

cgitb.enable()
form = cgi.FieldStorage()

qstring = os.environ['QUERY_STRING']
category = os.path.splitext(qstring.split('=')[1])[0]

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
	<p>Category {0} created successfully.</p>
	<a href="{0}">click here to go to new category</a>
</body>
</html>""".format(category)

print(output)

