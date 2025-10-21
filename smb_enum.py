# smb_enum.py
import subprocess
import os

def run_enum(target_ip):
    print(f"[+] Enumerating SMB on {target_ip}")

    out_file = f"logs/smb_enum_{target_ip}.txt"
    with open(out_file, "w") as f:
        try:
            # Null session user enum
            f.write(f"== enum4linux-ng ==\n")
            subprocess.run(["enum4linux-ng", target_ip], stdout=f, stderr=subprocess.DEVNULL)

            # Shares
            f.write(f"\n== smbclient -L ==\n")
            subprocess.run(["smbclient", "-L", f"//{target_ip}/", "-N"], stdout=f, stderr=subprocess.DEVNULL)

        except Exception as e:
            print(f"[-] Error: {e}")

if __name__ == "__main__":
    with open("logs/ips.txt") as f:
        for line in f:
            ip = line.strip()
            run_enum(ip)
