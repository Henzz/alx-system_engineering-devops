# Execute the pkill command to kill the process name 'killmenow'
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/bin', '/bin'],
  onlyif  => 'pgrep killmenow',
}
