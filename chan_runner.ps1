# chain_runner.ps1
Write-Host "[*] Running Subdomain Enumeration..."
python .\subdomain_enum.py

Write-Host "[*] Running SMB Enumeration..."
python .\smb_enum.py

Write-Host "[*] Dumping LDAP Info..."
python .\ldap_dump.py

Write-Host "[*] Extracting AS-REP Roastable Users..."
python .\asrep_extractor.py

Write-Host "[*] Enumerating SNMP..."
python .\snmp_enum.py
