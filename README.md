# 🛡️ joshxss - Automated XSS Scanner

**joshxss** is a fast, customizable XSS (Cross-Site Scripting) scanner built by @Josh as part of the HACKERMIND X toolset. It automates the process of detecting reflected XSS vulnerabilities in URLs and parameters using smart payload injection and response analysis.

---

## 🚀 Features

- 🔍 Scans URLs with GET parameters for reflected XSS.
- 💉 Injects payloads into each parameter.
- ⚡ Detects reflected payloads and basic context (HTML, JS, etc.).
- 🧠 Smart reflection matching with optional keyword triggers.
- 🧰 Supports custom payloads file.
- 📄 Generates simple report/log output.

---

## 🧑‍💻 Usage


 python3 joshxss.py -u "https://example.com/page.php?query=test"

## ⚠️ Disclaimer

This tool is for **educational and authorized penetration testing** only.

Using it on systems without permission is **illegal and unethical**. JoshXSS was built with the sole intent of empowering ethical hackers and security researchers to test their own environments or with explicit permission.
