# subdomain_enum.py
import requests
import dns.resolver
import dns.query
import dns.zone
import socket
import sys

WORDLIST = ["admin", "dev", "test", "vpn", "mail"]
TIMEOUT = 2
TARGET_DOMAIN = "target.com"
RESOLVER = dns.resolver.Resolver()

def passive_crtsh(domain):
    print(f"[+] Passive: Fetching subdomains from crt.sh")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        r = requests.get(url, timeout=TIMEOUT)
        entries = set()
        if r.ok:
            for entry in r.json():
                name = entry['name_value'].split('\n')[0]
                if domain in name:
                    entries.add(name.strip())
        return list(entries)
    except Exception as e:
        print(f"[-] Error: {e}")
        return []

def active_bruteforce(domain):
    print(f"[+] Active: Bruteforcing subdomains")
    found = []
    for sub in WORDLIST:
        fqdn = f"{sub}.{domain}"
        try:
            answers = RESOLVER.resolve(fqdn, 'A')
            for rdata in answers:
                print(f"    [+] Found: {fqdn} ➜ {rdata}")
                found.append(fqdn)
        except:
            pass
    return found

def try_zone_transfer(domain):
    print(f"[+] Checking for zone transfer...")
    try:
        ns_answers = RESOLVER.resolve(domain, 'NS')
        for ns in ns_answers:
            ns_ip = socket.gethostbyname(str(ns))
            print(f"    [+] Trying AXFR on {ns} ({ns_ip})")
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns_ip, domain, timeout=5))
                for name, node in zone.nodes.items():
                    fqdn = f"{name}.{domain}"
                    print(f"    [AXFR] {fqdn}")
            except Exception as e:
                print(f"    [-] AXFR failed: {e}")
    except:
        print("[-] Could not fetch NS records")

if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else TARGET_DOMAIN

    passive = passive_crtsh(domain)
    brute = active_bruteforce(domain)
    try_zone_transfer(domain)

    all_found = set(passive + brute)
    with open("logs/dns_enum.txt", "w") as f:
        for sub in all_found:
            f.write(sub + "\n")

    print(f"[+] Total found: {len(all_found)}")
