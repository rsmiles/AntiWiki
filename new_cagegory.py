import cgi, cgitb, os
from lib import *
from config import *

cgitb.enable()
form = cgi.FieldStorage()

qsring = os.environ['QUERY_STRING']
folder = os.path.splitext(qstring.split('=')[0]

os.mkdir(WEB_ROOT + 'Pages/' + folder)

output = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<body>
	
</body>
</html>\
""".format(result)

print(output)
