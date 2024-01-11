# 0x10-https_ssl

## Tasks
1. [World Wide Web](./0-world_wide_web)
**Requirements:**

1. Add the subdomain www to your domain, pointing it to lb-01 IP.
2. Add the subdomains lb-01, web-01, and web-02 to your domain, pointing them to their respective IPs.
3. Write a Bash script (`0-world_wide_web`) accepting two arguments:
   - `domain`: domain name to audit (mandatory).
   - `subdomain`: specific subdomain to audit (optional).


---

2. [HAProxy SSL Termination](./1-haproxy_ssl_termination)
**Requirements:**

1. Install HAProxy version 1.5 or higher.
2. Create a certificate using Certbot.
3. Configure HAProxy to:
   - Listen on port TCP 443.
   - Accept SSL traffic.
   - Serve encrypted traffic returning the root of your web server.
   - Ensure querying the root of your domain displays a page containing "Holberton School."
4. Share HAProxy config as an answer file (`/etc/haproxy/haproxy.cfg`).
