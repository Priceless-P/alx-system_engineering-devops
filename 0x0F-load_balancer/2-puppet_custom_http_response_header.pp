# Creates a custom HTTP header response with Puppet.
exec { 'command':
  command  => 'sudo apt-get update -y;
  sudo apt-get install nginx -y;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
