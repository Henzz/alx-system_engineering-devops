# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

# Create the holberton user
user { 'holberton':
  ensure => present,
}

# Set appropriate permission for the file to access
file { '/etc/passwd':
  ensure  => present,
  content => 'File content goes here',
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0755',
}

# Ensure the 'holberton' user can log in without any errors
exec { 'set_holberton_password':
  command => 'echo "holberton:password" | chpasswd',
  require => User['holberton'],
}

