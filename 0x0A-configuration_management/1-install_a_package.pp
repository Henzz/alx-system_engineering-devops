# Using Puppet installs a flask from pip3 with specific version

# Resource class for managing pip packages
package { 'python3-pip':
  ensure => installed,
}

# Resource to install flask with a specific version
package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
