# gitlab_scan
Extremely useful cybersecurity oriented framework for Gitlab investigating. One includes 15 modules and may be enhanced by everyone!

One should write the values in access_tokens.py.

To get geolocation data [users, runners] one should get access tokens in https://abuseipdb.com, https://ipgeolocation.io and/or https://ipapi.com. One should keep in mind the limits for API requests amount. With empty values of abuseipdb_token, ipgeolocation_token and ipapi_token one will get users/runners IPs only.

It is possible to ignore hosts and countries determined in access_tokens.py.

Run command: python3 gitlab_scan.py
