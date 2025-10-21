# ldap_dump.py
from ldap3 import Server, Connection, ALL, ANONYMOUS
import sys

def ldap_enum(ip):
    print(f"[+] LDAP enum on {ip}")
    server = Server(ip, get_info=ALL)
    conn = Connection(server, authentication=ANONYMOUS, auto_bind=True)

    # Search for users
    conn.search(search_base='dc=example,dc=com',
                search_filter='(objectClass=user)',
                attributes=['sAMAccountName', 'userAccountControl'])

    roastable_users = []
    with open(f"logs/ldap_dump_{ip}.txt", "w") as f:
        for entry in conn.entries:
            user = entry['sAMAccountName']
            uac = int(str(entry['userAccountControl']))
            if (uac & 0x00200000) == 0:
                f.write(f"[+] User: {user}\n")
                roastable_users.append(str(user))
            else:
                f.write(f"[-] Skipped SPN: {user}\n")

    return roastable_users

if __name__ == "__main__":
    with open("logs/ips.txt") as f:
        for line in f:
            ip = line.strip()
            roastables = ldap_enum(ip)
            with open("logs/asrep_candidates.txt", "a") as r:
                for user in roastables:
                    r.write(f"{user}@{ip}\n")
