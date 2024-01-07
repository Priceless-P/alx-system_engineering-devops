# 0x0C-web_server

## Tasks

1. [Transfer a file to your server (0-transfer_file)](0-transfer_file)
    - **Requirements:**
        - Accepts 4 parameters: path to the file, server IP, username for scp, path to the SSH private key.
        - Display Usage if less than 3 parameters passed.
        - Transfer the file to the user's home directory using `scp`.
        - Disable strict host key checking when using `scp`.

2. [Install Nginx web server (1-install_nginx_web_server)](1-install_nginx_web_server)
    - **Requirements:**
        - Install NGINX on web-01 server.
        - NGINX should listen on port 80.
        - Upon querying NGINX at root (/) with a GET request using curl, it must return a page containing the string "Hello World!".
        - Configuration should be done via a Bash script without using systemctl for restarting NGINX.

3. [Setup a domain name (2-setup_a_domain_name)](2-setup_a_domain_name)
    - **Requirements:**
        - Provide a domain name without a subdomain.
        - Configure DNS records with an A entry so that the root domain points to web-01 IP address.
        - Verification of the Registrar should show "registrarName": "Dotserve Inc" in the JSON response.

4. [Redirection (3-redirection)](3-redirection)
    - **Requirements:**
        - Configure NGINX to redirect /redirect_me to another page with a "301 Moved Permanently" status code.
        - Bash script containing commands to configure a new Ubuntu machine to meet the redirection requirement.

5. [Not found page 404 (4-not_found_page_404)](4-not_found_page_404)
    - **Requirements:**
        - Configure NGINX to have a custom 404 page returning an HTTP 404 error code.
        - The page must contain the string "Ceci n'est pas une page".
        - Bash script to configure a new Ubuntu machine to meet the custom 404 page requirement.

6. [Install Nginx web server with Puppet (7-puppet_install_nginx_web_server)](7-puppet_install_nginx_web_server.pp)
    - **Requirements:**
        - Use Puppet to install NGINX on web server.
        - NGINX should listen on port 80.
        - When querying NGINX at root (/) with a GET request using curl, it must return a page containing the string "Hello World!".
        - Implement a "301 Moved Permanently" redirection for /redirect_me.
