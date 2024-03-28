# Using Puppet installs a flask from pip3 with specific version

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask with a specific version using pip3 provider
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
