# This Puppet manifest updates the Nginx configuration file and sets ULIMIT="-n 4096"

# Update ULIMIT in /etc/default/nginx
file_line { 'set_ulimit':
  path   => '/etc/default/nginx',
  line   => 'ULIMIT="-n 4096"',
  match  => '^ULIMIT=',
  ensure => present,
}

