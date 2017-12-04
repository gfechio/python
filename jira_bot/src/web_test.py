import os
import sys

import urllib2

def run(proxy, url):
    url = url.replace("\\","").replace("$","")
    proxy_support = urllib2.ProxyHandler({"http":"http://"+proxy+":3128"} )
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    sys.stdout.write("Testing URL -> "+url+" on proxy ->"+proxy+"\n")
    try:
        urllib2.urlopen("http://"+url)
	return "NOK"
    except urllib2.HTTPError, err:
        if err.code == 403:
            return "OK"
        else:
            return "NOK"
