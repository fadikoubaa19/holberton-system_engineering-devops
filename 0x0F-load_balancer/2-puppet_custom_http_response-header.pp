# HEre we are ome puppet

exec {'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
-> package {'nginx':
  ensure => present,
}
-> file_line {'head':
  esure => present,
  path  => '/etc/nginx/site-available/default',
  line  => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
  }
 -> exec { 'Ngin':
  command  => 'sudo service nginx restart',
  provider => shell,
}
