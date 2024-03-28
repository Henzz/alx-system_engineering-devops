# Using Puppet installs a flask from pip3 with specific version

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Execute command to install Flask with a specific version using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  creates => '/usr/local/lib/python3.9/dist-packages/flask',
  require => Package['python3-pip'],
}
