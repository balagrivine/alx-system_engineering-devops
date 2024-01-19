#a puppet manifest to kill process named killmenow

exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
