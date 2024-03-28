# Create a puppet file in /tmp with file permission 0744
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
