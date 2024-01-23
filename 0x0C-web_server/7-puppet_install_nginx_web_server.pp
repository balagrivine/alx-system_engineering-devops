#!/usr/bin/python3
#puppet script to install Nginx and configure it for a redirect from redirect_me/

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

pacckage { 'nginx':
  require => 'Exec['apt update']',
  ensure  => installed,
}

file { 'Root page':
  ensure  => present,
  path    => '/vaw/www/html/index.html',
  content => 'Hello World!',
}

exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

file { 'error file':
  ensure  => present,
  content => 'Ceci n'est pas une page\n', 
}

file { 'Nginx default config file':
  ensure  => present,
  path    => '/etc/nginx/sites-enabled/default',
  content => 'server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files $uri $uri/ =404;
        }
	error_page 404 /404.html;
	location /404.html {
		internal;
	}
	if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}'
}

exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
