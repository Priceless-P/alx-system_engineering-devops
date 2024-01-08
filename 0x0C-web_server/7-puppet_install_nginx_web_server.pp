# Install and configure Nginx with Puppet.
package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 https://www.google.com/;
    }

    error_page 404 /404.html;

    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/usr/share/nginx/html/404.html':
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
