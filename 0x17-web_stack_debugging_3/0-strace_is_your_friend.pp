# Workpress website 500 error fix
# This Puppet manifest renames occurrences of 'phpp' to 'php' in the file 'wp-settings.php'

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
}
