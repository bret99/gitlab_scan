# gitlab_scan
Extremely useful cybersecurity oriented framework for Gitlab investigating. One includes 15 modules and may be enhanced by everyone!

One should write the values in access_tokens.py.

To get geolocation data [users, runners] one should get access tokens in https://abuseipdb.com and/or https://ipgeolocation.io. One should keep in mind the limits for API requests amount. With empty values of abuseipdb_token and ipgeolocation_token one will get users/runners IPs only.

Run command: python3 gitlab_scan.py
