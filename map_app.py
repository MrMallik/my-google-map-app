import sys
import urllib.parse as url
from datetime import datetime
import webbrowser

def getQuery():
    if len(sys.argv) > 1:
        s = ' '.join(sys.argv[1:])
        return  s
    
    else:
        print("No query given. Give atleast 1 query")
        sys.exit()


def genUrl(query):
    return 'https://www.google.com/maps/search/?api=1&query=' + url.quote_plus(query)

def logQuery(query):
    fh = open('queryLog.log', 'a')
    now = datetime.now()
    now = now.strftime('%dth %B, %Y @ %H:%M')
    fh.write(now + " : \'"+query+"\'" + "\n\n")
    fh.close()

q = getQuery()
logQuery(q)
webbrowser.open(genUrl(q))
