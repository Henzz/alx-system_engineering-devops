# Client SSH configuration file to connect to a server without typing a password with puppet file
file { '/etc/ssh/ssh_config':
  ensure => file,
  owner => 'ubuntu',
  group => 'root',
  mode => '0600',
  content => "
    Host 54.227.128.255
        HostName 54.227.128.255
        User ubuntu
        IdentityFile ~/.ssh/school
        PreferredAuthentication publickey
        PasswordAuthentication no
  ",
}
