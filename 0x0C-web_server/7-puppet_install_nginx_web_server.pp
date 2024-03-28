# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "# Nginx configuration file
server {
    listen 80;
    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 http://example.com/redirected_page;
    }
}",
  require => Package['nginx'],
}

# Enable the default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
