# gitlab_scan
Extremely useful cybersecurity oriented framework for Gitlab investigating. One includes 17 modules and may be enhanced by everyone!

One should write the values in access_tokens.py.

To get geolocation data [users, runners] one should get access tokens in https://abuseipdb.com, https://ipgeolocation.io and/or https://ipapi.com. One should keep in mind the limits for API requests amount. With empty values of abuseipdb_token, ipgeolocation_token and ipapi_token one will get users/runners IPs only.

It is possible for modules 4 and 16 to ignore hosts and countries determined in access_tokens.py.

Run command:
```
python3 gitlab_scan.py
```

---

## 💎 Support the Project

If this tool helps protect your infrastructure, consider supporting the developer! 

### Crypto Wallets
| Asset | Network | Address |
| :--- | :--- | :--- |
| **BTC** | Bitcoin | `bc1qjwl80sv06xj2yhumn6k6xemchryem923wwts5x` |
| **USDT / ETH** | Ethereum (ERC20) | `0xc01b996c7b08ccfad463f27e54f1e74e6ac6f9ff` |
| **USDT / SOL** | Solana | `D7a5CdLaDwkKehnH82y6VJEF3hADWuupuhWCXecHvEnt` |
| **TON** | TON Network | `UQBhPLwdFiJdh6sZ96sZfxrxD9Lu6NFtaUecWeoHSM-EPc0P` |
| **LTC** | Litecoin | `ltc1qkm58ks5kuc64rjwd74sfalc5xsn7h6sr4vt45w` |
| **SOL** | Solana | `D7a5CdLaDwkKehnH82y6VJEF3hADWuupuhWCXecHvEnt` |

---

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
