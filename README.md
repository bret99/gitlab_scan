# gitlab_scan (GitLab Security Auditing & OSINT Framework)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)

`gitlab_scan` is a zero-dependency, highly extensible security framework designed for thorough reconnaissance, compliance auditing, and threat hunting across GitLab instances. Equipped with 17 specialized modules, the framework allows security operations (SecOps) teams, penetration testers, and system administrators to audit users, pipelines, runners, and configuration vulnerabilities.

The framework features built-in support for threat intelligence enrichment, mapping discovered infrastructure, user sessions, and CI/CD runner environments against geolocation and IP reputation databases.

## 🧩 Architecture & Modules

The framework's extensible architecture includes 17 native assessment modules covering:
- User enumeration, session tracking, and access control validation.
- CI/CD Runner environment analysis, metadata harvesting, and network exposure mapping.
- Threat intelligence integration for public-facing GitLab entry points.
- Customizable filtering to ignore specific trusted hosts or entire countries (supported natively in Module 4 and Module 16).

## 🚀 Threat Intelligence & Geolocation Enrichment

To enrich gathered data (such as user logons or CI/CD runner endpoints) with geolocation and risk metadata, `gitlab_scan` integrates with premier IP intelligence providers. If no tokens are specified, the tool will gracefully fall back to displaying raw IP addresses.

| Provider | Purpose | Default Free Tier Quota Limits |
| :--- | :--- | :--- |
| **AbuseIPDB** | Malicious IP reputation & threat scoring | 1,000 requests per day / 30,000 per month |
| **IPGeolocation** | Advanced coordinate, ISP, and country mapping | 1,000 requests per day / 30,000 per month |
| **ipapi** | Fast fallback network and location metadata | 1,000 requests per month |

## 🛠️ Installation & Configuration

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/bret99/gitlab_scan.git](https://github.com/bret99/gitlab_scan.git)
   cd gitlab_scan
   ```

2. **Configure Access Tokens:**
   
   Open `access_tokens.py` to supply your credentials and adjust parameters:
   ```python
   gitlab_access_token = "" # one should insert gitlab token here 
   gitlab_server_address = "" # [https://gitlab.example.com](https://gitlab.example.com)

   # Threat Intelligence & Geolocation Tokens (Optional)
   abuseipdb_token = "" # [https://www.abuseipdb.com](https://www.abuseipdb.com); 1000 per day, 30000 per month limited
   ipgeolocation_token = "" # [https://ipgeolocation.io](https://ipgeolocation.io); 1000 per day, 30000 per month limited
   ipapi_token = "" # [https://ipapi.com](https://ipapi.com); 1000 per month limited

   # Module 4 & 16 Exclusion Whitelists
   hosts_to_ignore = [] # example: ["192.168.0.23", "none", "None"]
   countries_to_ignore = [] # example: ["us", "none"]
   ```

## 💻 Usage

`gitlab_scan` operates with a zero-external-dependency footprint using standard Python libraries, facilitating instant standalone execution. Run the primary entry point to start the interactive management shell:

```bash
python3 gitlab_scan.py
```

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
