# ?? Chain Attack Tool Ч Full Protocol Enumeration & Exploitation Chain
> Simulated real-world attack chain involving enumeration and initial access across key protocols: **DNS ? SMB ? LDAP ? Kerberos ? SNMP**
____________________________________________________________________________________________________________________________________________________________________
## ?? Objective
Conduct a chained protocol attack simulation within a test or lab environment using Python scripts that automate and log reconnaissance activities across the network stack. This reflects techniques often used in red team ops and post-exploitation lateral movement.
____________________________________________________________________________________________________________________________________________________________________
## ?? Structure
/chain_attack_tool/
??? subdomain_enum.py # DNS/Subdomain Recon
??? smb_enum.py # SMB Shares & User Enum
??? ldap_dump.py # LDAP Info Gathering
??? asrep_extractor.py # Kerberos AS-REP Roastable Users
??? snmp_enum.py # SNMP Router/Device Enumeration
??? chain_runner.ps1 # PowerShell runner (Windows)
??? logs/ # All output logs from modules
??? captures/ # Packet dumps or session evidence
??? tmp_users.txt # Intermediate user list
??? report.md # Final operation-style report

________________________________________________________________________________________________________________________________
## ??? Execution Chain Summary
### ?? 1. `subdomain_enum.py` Ч DNS Recon
- Used `dns.resolver` to enumerate valid subdomains from a wordlist.
- Resolved A records to IPs.
- Logs stored in `logs/dns_enum.log`.

? **Findings**:
- 12 subdomains discovered
- 4 subdomains pointed to internal IP ranges (10.x.x.x)
________________________________________________________________

### ?? 2. `smb_enum.py` Ч SMB Enumeration

- Queried SMB port (445) across discovered hosts.
- Checked for open shares (null session allowed).
- Pulled list of users via `srvsvc` and `samr` protocols.

? **Findings**:
- `IPC$`, `Public` share open
- 7 usernames extracted (stored in `tmp_users.txt` and `logs/smb_enum.log`)
________________________________________________________
### ?? 3. `ldap_dump.py` Ч LDAP Recon
- Connected anonymously to port 389
- Queried for `sAMAccountName`, `userPrincipalName`, and group membership

? **Findings**:
- Confirmed anonymous bind on LDAP
- Mapped out 4 users with no `pwdLastSet` and no `requirePreAuth`
- Exported in `logs/ldap_dump.json`
_________________________________________________________
### ?? 4. `asrep_extractor.py` Ч Kerberos AS-REP Roasting
- Took usernames from `tmp_users.txt`
- Queried KDC for AS-REP without pre-auth
- Captured TGT-like hashes

? **Findings**:
- 2 users vulnerable to AS-REP Roasting
- Hashes saved to `logs/asrep_hashes.txt`
- Crackable with `hashcat` using mode 18200

Example hash: $krb5asrep$23$user@domain:12345678abcdef.
______________________________________________________________
### ?? 5. `snmp_enum.py` Ч SNMP Information Leakage
- Used default `public` community string on port 161
- Pulled system info via `snmpwalk`

? **Findings**:
- Found device hostname: `core-router-1`
- Detected network interfaces and routing table
- Possible pivot point to other subnets (e.g., 172.16.1.0/24)

________________________________________________________________________________________________________________________________
## ?? Chained Attack Flow
[DNS/Subdomain Recon]
?
[SMB Null Session ? User Enum]
?
[LDAP Anonymous Bind ? Detailed User Info]
?
[Kerberos AS-REP ? Offline Hash Extraction]
?
[SNMP Router Info ? Lateral Movement Plan]

ннннннннннннннннннннннннннн________________________________________________________________________________________________________________________________

## ?? Tools/Modules Used

| Module              | Protocol | Purpose                     |
|---------------------|----------|-----------------------------|
| `subdomain_enum.py` | DNS      | Subdomain + IP Resolution   |
| `smb_enum.py`       | SMB      | Null session, user enum     |
| `ldap_dump.py`      | LDAP     | User data, groups, info     |
| `asrep_extractor.py`| Kerberos | AS-REP roastable users      |
| `snmp_enum.py`      | SNMP     | Network device enumeration  |

____________________________________________________________________________________________________________________________________________________________________
## ?? Output Files

| Location      | Description                         |
|---------------|-------------------------------------|
| `logs/`       | Logs for each stage                 |
| `captures/`   | PCAPs or SNMPwalk dumps             |
| `tmp_users.txt` | Intermediate user list            |

________________________________________________________________________________________________________________________________
## ??? Recommendations (if real-world)

- **Restrict anonymous SMB & LDAP access**
- **Use strong passwords + disable pre-auth opt-outs**
- **Harden SNMP config: change community string, ACLs**
- **Segment internal zones & reduce exposure**

__________________________________________________________________________________________________________________________________________________________________
## ?? Notes
- All scripts are standalone and modular.
- Designed for lab use and **educational red team simulations**.
- For use in lawful environments only.
нннннннннннннннннннннннннннннннн________________________________________________________________________________________________________________________________
## ?? Next Steps

- Add CLI arguments and `--help` to each script
- Combine logs into a final timeline
- Add password cracking via `hashcat` automation (future module)

____________________________________________________________________________________________________________________________________________________________________

## ?? Authored By

**Rossu** Ч Offensive Security Developer & Protocol Chain Master  
??? GitHub: [your GitHub URL]  
??? Focus: Red Team scripting, protocol exploitation, chained recon, adversary simulation