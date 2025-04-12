# DWAYNE Scoring Engine Config Cheat Sheet

## Service Checks

### DNS
```properties
[[box.dns]]
port = 53          # Port for DNS service (default is 53)

    [[box.dns.record]]
    kind = "A"     # Address record, maps a domain name to an IPv4 address
    domain = "example.com"
    answer = ["192.168.1.1"]

    [[box.dns.record]]
    kind = "AAAA"  # IPv6 address record, maps a domain name to an IPv6 address
    domain = "example.com"
    answer = ["2001:0db8:85a3:0000:0000:8a2e:0370:7334"]

    [[box.dns.record]]
    kind = "CNAME" # Canonical name record, maps a domain name to another domain name (alias)
    domain = "www.example.com"
    answer = ["example.com"]

    [[box.dns.record]]
    kind = "MX"    # Mail exchange record, specifies mail servers for the domain
    domain = "example.com"
    answer = ["mail.example.com"]

    [[box.dns.record]]
    kind = "TXT"   # Text record, holds arbitrary text data (often used for verification and security)
    domain = "example.com"
    answer = ["v=spf1 include:_spf.example.com ~all"]

    [[box.dns.record]]
    kind = "NS"    # Name server record, specifies the authoritative name servers for the domain
    domain = "example.com"
    answer = ["ns1.example.com", "ns2.example.com"]

    [[box.dns.record]]
    kind = "SRV"   # Service record, specifies the location of services (e.g., SIP, XMPP) for the domain
    domain = "_sip._tcp.example.com"
    answer = ["10 60 5060 sipserver.example.com"]

    [[box.dns.record]]
    kind = "PTR"   # Pointer record, maps an IP address to a domain name (reverse DNS lookup)
    domain = "1.1.168.192.in-addr.arpa"
    answer = ["example.com"]
```

### FTP
```properties
[[box.ftp]]
port = 21          # Port for FTP service (default is 21)
anonymous = false  # Allow anonymous login (default is false)

    [[box.ftp.file]]
    name = "memo.txt" # File to retrieve
    hash = "9d8453505bdc6f269678e16b3e56c2a2948a41f2c792617cc9611ed363c95b63" # SHA256 sum to compare to

    [[box.ftp.file]]
    name = "workfiles.txt" # File to retrieve
    regex = "work.*work"   # Regex to test against file
```

### IMAP
```properties
[[box.imap]]
port = 143         # Port for IMAP service (default is 143)
encrypted = false  # Use encrypted connection (default is false)
```

### LDAP
```properties
[[box.ldap]]
port = 636         # Port for LDAP service (default is 636)
encrypted = true   # Use encrypted connection (default is false)
domain = "example.com" # Domain for LDAP service
```

### Ping
```properties
[[box.ping]]
count = 1              # Number of ping attempts (default is 1)
allowpacketloss = false # Allow packet loss (default is false)
percent = 50           # Max percent packet loss allowed
```

### RDP
```properties
[[box.rdp]]
port = 3389         # Port for RDP service (default is 3389)
```

### SMB
```properties
[[box.smb]]
port = 445          # Port for SMB service (default is 445)
anonymous = false   # Allow anonymous login (default is false)
credlists = ["admins",] # Credential list to use

    [[box.smb.file]]
    name = "memo.txt"
    hash = "9d8453505bdc6f269678e16b3e56c2a2948a41f2c792617cc9611ed363c95b63"

    [[box.smb.file]]
    name = "workfiles.txt"
    regex = "work.*work"
```

### SMTP
```properties
[[box.smtp]]
port = 25           # Port for SMTP service (default is 25)
encrypted = false   # Use encrypted connection (default is false)
sender = "hello@scoring.engine"
receiver = "tuck@example.com"
body = "Test email body"
```

### SQL
```properties
[[box.sql]]
kind = "mysql"      # Type of SQL database (default is mysql)

    [[box.sql.query]]
    contains = true
    database = "wordpress"
    table = "users"
    column = "username"
    output = "Tuck"

    [[box.sql.query]]
    database = "squirrelmail"
    table = "senders"
    column = "name"
    output = "Toby Turtle" # Must match exactly

    [[box.sql.query]]
    database = "wordpress"
    databaseexists = true # Simply checks if database exists with "show databases;"
```

### SSH
```properties
[[box.ssh]]
port = 22           # Port for SSH service (default is 22)
privkey = "example_sshkey" # Name of private key in checkfiles/
username = "exampleuser"

    [[box.ssh.command]]
    command = "cat /etc/passwd"
    contains = true
    output = "root:"

    [[box.ssh.command]]
    useregex = true
    command = "getent passwd"
    output = '\w.*:[1-9].*:.*'
```

### TCP
```properties
[[box.tcp]]
port = 4444         # Port for TCP service
```

### VNC
```properties
[[box.vnc]]
port = 5901         # Port for VNC service (default is 5900)
```

### Web
```properties
[[box.web]]
port = 80           # Port for web service (default is 80)
scheme = "http"     # Scheme for web service (default is http)
credlists = ["web",] # Credential list to use

    [[box.web.url]]
    path = "/joomla"
    regex = ".*easy to get started creating your website.*"

    [[box.web.url]]
    path = "/wp-admin.php"
    usernameparam = "user"
    passwordparam = "pw"
    status = 302
```

### WinRM
```properties
[[box.winrm]]
port = 5985         # Port for WinRM service (default is 5985)
encrypted = true    # Use encrypted connection (default is false)
badattempts = 1     # Number of bad login attempts allowed

    [[box.winrm.command]]
    command = "Get-FileContent memo.txt"
    contains = true
    output = "business as usual in the kingdom!"
```