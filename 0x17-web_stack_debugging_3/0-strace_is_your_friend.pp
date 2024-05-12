# Wordpress website running on a LAMP stack error 500 fix

file { '/www/html/wp-settings.php':
  ensure => file,
  content => replace(file('/www/html/wp-settings.php'), 'phpp', 'php'),
}
