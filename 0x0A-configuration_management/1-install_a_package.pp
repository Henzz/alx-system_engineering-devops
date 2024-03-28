# Using Puppet installs a flask from pip3 with specific version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
