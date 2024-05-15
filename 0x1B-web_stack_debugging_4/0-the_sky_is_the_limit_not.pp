# Nginx configuration update on benchmarking test with ApacheBench failed request fix

class nginx_config {
  # Update ULIMIT in /etc/default/nginx
  file_line { 'nginx_ulimit':
    path   => '/etc/default/nginx',
    line   => 'ULIMIT="-n 4096"',
    match  => '^#?ULIMIT=',
    ensure => present,
  }
}
