# 0x09. Web infrastructure design

### Task 0: [Simple Web Stack](./0-simple_web_stack)

#### Overview:
This task involves designing a one-server web infrastructure using a LAMP stack. The goal is to host the website www.foobar.com.

#### Components:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (code base)
- 1 database (MySQL)
- 1 domain name (foobar.com) with a www record pointing to the server's IP (8.8.8.8)

#### Specifics:
- **Server:** Physical or virtual machine hosting the entire infrastructure.
- **Domain Name:** Human-readable alias (www.foobar.com) pointing to the server's IP.
- **DNS Record:** Typically a CNAME or A record, specifying the www subdomain.
- **Web Server:** Nginx handling HTTP requests, serving static content.
- **Application Server:** Processing dynamic content, running the code base.
- **Database:** MySQL storing and retrieving data for the website.
- **Communication:** The server communicates with user computers using the HTTP protocol.

#### Issues:
- **SPOF:** Single Point of Failure with a single server.
- **Downtime during Maintenance:** Server restarts required during code deployment.
- **Scalability Issues:** Difficulty handling increased traffic.

### Task 1: [Distributed Web Infrastructure](./1-distributed_web_infrastructure)

#### Overview:
Design a three-server web infrastructure hosting www.foobar.com. Focus on distribution, load balancing, and database replication.

#### Components:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load balancer (HAproxy)
- 1 set of application files (code base)
- 1 database (MySQL)

#### Specifics:
- **Load Balancer:** Distributes traffic across multiple servers for performance and redundancy.
- **Distribution Algorithm:** Configured on the load balancer for effective load distribution.
- **Active-Active or Active-Passive Setup:** Active-Active setup
- **Primary-Replica (Master-Slave) Cluster:** Involves a primary server handling write operations and replicating changes to multiple replica servers.
- **Primary vs. Replica Nodes:**
    - **Primary Node:** Handles writes, serves as the authoritative source for data changes, and requires high availability for maintaining application consistency.
    - **Replica Node:** Handles reads, receives replicated data, serves reads, improves scalability, and can act as a backup, supporting fault tolerance in case of primary node failure.

#### Issues:
- **SPOF:** Potential single points of failure in the infrastructure (Load balancer).
- **Security Issues:** Lack of firewall and HTTPS.
- **No Monitoring:** Absence of monitoring for issue detection and resolution.

### Task 2: [Secured and Monitored Web Infrastructure](./2-secured_and_monitored_web_infrastructure)

#### Overview:
Design a secured and monitored three-server web infrastructure hosting www.foobar.com with firewalls, HTTPS, and monitoring.

#### Components:
- 3 firewalls
- 1 SSL certificate for HTTPS
- 3 monitoring clients (Sumo Logic or other services)
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 database (MySQL)

#### Specifics:
- **Firewalls:** Enhance security by controlling incoming and outgoing traffic.
- **SSL Certificate:** Encrypt traffic between users and the website for security.
- **Monitoring Clients:** Collect data for monitoring services like Sumo Logic.
- **Monitoring Purpose:** Detect and address issues, ensuring infrastructure health.
- **Monitoring Data Collection:** Monitoring tools collect data.
- **Monitoring Web Server QPS:** Set up monitoring for web server QPS (Queries Per Second).

#### Issues:
- **SSL Termination at Load Balancer Level:** Risks unencrypted traffic between the load balancer and internal servers.
- **Single MySQL Server for Writes:** A single point of failure, consider replication.
- **Uniform Servers:** Lack of diversity may pose security risks; diversifying components should be considered.