# 0x1A. Application server

This folder contains scripts and configuration files for setting up and deploying an application server using Python, Flask, Gunicorn, and Nginx.

### Task 0: Set up development with Python

This task involves setting up the development environment for an AirBnB clone application using Python and Flask.

- Ensure that SSH access to web-01 is configured.
- Install the `net-tools` package on your server.
- Clone the AirBnB_clone_v2 repository onto your web-01 server.
- Configure the Flask application to serve content from the route `/airbnb-onepage/` on port 5000.

### Task 1: Set up production with Gunicorn

- Install Gunicorn and any required libraries.
- Configure Gunicorn to serve the same content from the same route as in Task 0.
- Ensure Gunicorn binds to localhost on port 5000.
- Verify that the application is working by binding a Gunicorn instance to localhost and sending requests.

### Task 2: [Serve a page with Nginx](./2-app_server-nginx_config)

- Configure Nginx to serve the application both locally and on its public IP on port 80.
- Proxy requests to the process listening on port 5000.

### Task 3: [Add a route with query parameters](./3-app_server-nginx_config)

This task expands the web application by adding another service to handle odd or even integers.

- Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.
- Serve the content both locally and on the public IP on port 80.

### Task 4: [Serve your AirBnB clone](./4-app_server-nginx_config)

- Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Set up Nginx to proxy requests to the root URL to the Gunicorn instance.
- Ensure Nginx properly serves the static assets found in `web_dynamic/static/`.
- Update `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.

### Task 6: [Deploy it!](./gunicorn.service)

This task is on setting up the application server to run by default when Linux is booted using systemd.

- Write a systemd script to start a Gunicorn process to serve the content.
- Ensure the Gunicorn process spawns 3 worker processes and logs errors and access.
- Store the systemd script in the appropriate directory on web-01.
- Start the systemd service and leave it running.

### Task 7: [No service interruption](./4-reload_gunicorn_no_downtime)

This task involves writing a Bash script to reload Gunicorn gracefully without service interruption.

- The script should gracefully restart Gunicorn without causing downtime.
- It should handle the progressive rollout of updates to Gunicorn workers.
