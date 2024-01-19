#create a file in temp

file { '/tmp/school':
  ensure  => 'file',
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
}
