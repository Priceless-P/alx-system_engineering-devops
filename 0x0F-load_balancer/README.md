# 0x0F. Load balancer

## Tasks

1. [0-custom_http_response_header](./0x0F-load_balancer/0-custom_http_response_header)
    - Configure Nginx to include a custom HTTP header (`X-Served-By`) on web-01 and web-02.
    - Create a Bash script to configure a new Ubuntu machine to meet the task requirements.

2. [1-install_load_balancer](./0x0F-load_balancer/1-install_load_balancer)
    - Install and configure HAproxy on lb-01 to distribute traffic to web-01 and web-02.
    - Implement round-robin load balancing algorithm.
    - Ensure HAproxy can be managed via an init script.
    - Write a Bash script to configure a new Ubuntu machine to fulfill the task requirements.

3. [2-puppet_custom_http_response_header.pp](./0x0F-load_balancer/2-puppet_custom_http_response_header.pp)
    - Automate the creation of a custom HTTP header (`X-Served-By`) using Puppet.
    - Configure a new Ubuntu machine to meet the task requirements.

