# This Puppet manifest updates the Nginx configuration file and sets ULIMIT="-n 4096"

# Add ULIMIT="-n 4096" if it does not exist
exec { 'add_ulimit_to_nginx':
  command => 'echo "ULIMIT=\"-n 4096\"" >> /etc/default/nginx',
  unless  => 'grep -q "^ULIMIT=\"-n 4096\"$" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

# Ensure file
file { '/etc/default/nginx':
  ensure  => file,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => File['/etc/default/nginx'],
}

