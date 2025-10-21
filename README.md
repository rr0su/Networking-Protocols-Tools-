# 🔗 chain_attack_tool

## 🔥 Full Protocol Attack Chain Toolkit

Performs DNS → SMB → LDAP → Kerberos → SNMP attack chain in real-world style.

### Modules

- `subdomain_enum.py` - DNS enum via crt.sh + bruteforce + AXFR
- `smb_enum.py` - SMB null session + share/user enum
- `ldap_dump.py` - Dump LDAP users, find AS-REP roast targets
- `asrep_extractor.py` - Extract Kerberos AS-REP hashes
- `snmp_enum.py` - Pull SNMP info from routers/devices
- `chain_runner.sh` - Run all tools in sequence

### 📁 Output

- `logs/`: Tool output (shares, users, SNMP, hashes)
- `captures/`: Hashes, PCAPs, creds

### 🧪 Recommended Lab Setup

- AD Lab (e.g., HackTheBox Forest or TryHackMe AttackBox)
- Router with SNMP (GNS3)
- Simulated DNS + Kerberos

---

## 📄 Final Report Template

```markdown
# 🧠 Red Team Report – Protocol Attack Chain

### Target: target.com

#### 1. DNS Enum:
- 17 subdomains found (crt.sh + brute)
- No zone transfer

#### 2. SMB Enum:
- Guest login on \\10.10.10.1
- User list extracted via enum4linux

#### 3. LDAP Dump:
- 47 users dumped
- Found 1 user roastable (no preauth): `svc_noroast`

#### 4. AS-REP Roast:
- Hash extracted for `svc_noroast`
- Hash cracked: Password = `Winter2023!`

#### 5. SNMP:
- SNMP exposed on 10.10.10.254
- Interface map + ARP table leaked

#### 🔗 Exploit Chain:
Initial → DNS → SMB enum → LDAP dump → AS-REP roast → SNMP network pivot

#### 📂 Artifacts:
- See `/logs/` and `/captures/` for full output
