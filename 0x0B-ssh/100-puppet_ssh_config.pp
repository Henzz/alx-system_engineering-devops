file { '':
  ensure => file,
  owner => 'ubuntu',
  group => '',
  mode => '0600',
  content => "
    Host 54.227.128.255
        HostName 54.227.128.255
        User ubuntu
        IdentityFile ~/.ssh/school
        PreferredAuthentications publickey
        PasswordAuthentication no
  ",
}
