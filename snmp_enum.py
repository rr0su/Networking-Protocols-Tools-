# snmp_enum.py
import subprocess

def run_snmp(ip):
    print(f"[+] Running SNMP enum on {ip}")
    out_file = f"logs/snmp_{ip}.txt"
    try:
        subprocess.run([
            "snmpwalk", "-v2c", "-c", "public", ip, "1"
        ], stdout=open(out_file, "w"))
    except Exception as e:
        print(f"[-] SNMP error: {e}")

if __name__ == "__main__":
    with open("logs/ips.txt") as f:
        for line in f:
            ip = line.strip()
            run_snmp(ip)
